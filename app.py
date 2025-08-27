from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# Veritabanı ayarları
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Veritabanı modeli (tablosu)
class Gorev(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gorev = db.Column(db.String(100), nullable=False)
    tamamlandi = db.Column(db.Boolean, default=False)
    # Yeni eklenecek kısım
    tarih = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<Gorev {self.id}>'

@app.route('/')
def index():
    yapilacaklar = Gorev.query.all()
    return render_template('index.html', yapilacaklar=yapilacaklar)

@app.route('/ekle', methods=['POST'])
def gorev_ekle():
    gorev_adi = request.form['gorev']
    # Tarih verisini formdan alıp datetime objesine çevirme
    gorev_tarihi = datetime.strptime(request.form['tarih'], '%Y-%m-%d')
    yeni_gorev = Gorev(gorev=gorev_adi, tarih=gorev_tarihi)
    db.session.add(yeni_gorev)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/sil/<int:id>', methods=['POST'])
def gorev_sil(id):
    gorev = Gorev.query.get_or_404(id)
    db.session.delete(gorev)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/guncelle/<int:id>', methods=['POST'])
def gorev_guncelle(id):
    gorev = Gorev.query.get_or_404(id)
    gorev.tamamlandi = not gorev.tamamlandi
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/api/gorevler')
def api_gorevler():
    gorevler = Gorev.query.all()
    takvim_verisi = []
    for gorev in gorevler:
        takvim_verisi.append({
            'title': gorev.gorev,
            'start': gorev.tarih.isoformat().split('T')[0], 
            'id': gorev.id
        })
    return jsonify(takvim_verisi)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
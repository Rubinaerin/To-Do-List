# To-do List Uygulaması

Bu proje, Python'ın **Flask** web framework'ü kullanılarak geliştirilmiş, tam işlevli bir yapılacaklar listesi uygulamasıdır. Kullanıcıların görevlerini eklemesine, silmesine, tamamlandı olarak işaretlemesine ve bu görevleri tarihleriyle birlikte bir takvimde görmesine olanak tanır.

## Özellikler

- **Görev Yönetimi:** Görevleri ekleyin, düzenleyin ve silin.
- **Kalıcı Veri Depolama:** Veriler, SQLite veritabanında kalıcı olarak saklanır.
- **Takvim Entegrasyonu:** Görevleri tarihlerine göre bir takvim görünümünde izleyin.
- **Kullanıcı Dostu Arayüz:** Bootstrap CSS framework'ü sayesinde modern ve duyarlı bir tasarıma sahiptir.

## Kurulum ve Başlatma

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin:

1.  **Depoyu Klonlayın:**
    ```bash
    git clone [https://github.com/Rubinaerin/To-Do-List.git](https://github.com/Rubinaerin/To-Do-List.git)
    cd To-Do-List
    ```

2.  **Sanal Ortam Oluşturun ve Etkinleştirin:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Gerekli Kütüphaneleri Yükleyin:**
    ```bash
    pip install Flask Flask-SQLAlchemy
    ```

4.  **Uygulamayı Çalıştırın:**
    ```bash
    python app.py
    ```

Uygulama çalıştıktan sonra tarayıcınızı açın ve `http://127.0.0.1:5000` adresine gidin.

## Kullanılan Teknolojiler

- **Python:** Programlama dili
- **Flask:** Web framework'ü
- **Flask-SQLAlchemy:** Veritabanı yönetimi için Flask uzantısı
- **SQLite:** Veritabanı
- **HTML, CSS, JavaScript:** Ön yüz teknolojileri
- **Bootstrap:** Arayüz tasarımı için CSS framework'ü
- **FullCalendar.io:** Takvim görünümü için JavaScript kütüphanesi
# FastApi_UrlShortener

# URL Kısaltma Servisi
Bu proje, FastAPI kullanılarak geliştirilmiş, kullanıcıların uzun URL'leri kısaltmalarını sağlayan ve kısaltılmış URL'ler üzerinden orijinal URL'lere yönlendirme yapan bir servistir.

# Özellikler
URL Kısaltma: Uzun URL'leri kısaltabilme.
Otomatik Yönlendirme: Kısaltılmış URL'lerin orijinal URL'lere yönlendirilmesi.
Başlangıç
Bu bölüm, projenin nasıl kurulacağını ve yerel bir sunucuda nasıl çalıştırılacağını adım adım açıklar.

# Gereksinimler
Python 3.6 veya üstü
pip (Python paket yöneticisi)
virtualenv (Sanal ortam oluşturucu)
# Kurulum Adımları
1. Sanal Ortam Oluşturma:
Projeyi izole bir ortamda çalıştırmak için Python sanal ortamı oluşturun:

bash
Copy code
'''python -m venv venv
source venv/bin/activate  # Unix veya MacOS için
venv\Scripts\activate     # Windows için '''
2. Bağımlılıkları Yükleme:
Projede kullanılan bağımlılıkları yükleyin:

bash
Copy code
pip install -r requirements.txt
3. Uygulamayı Çalıştırma:
Uygulamayı başlatmak için aşağıdaki komutu kullanın:

bash
Copy code
uvicorn main:app --reload
Uygulama http://127.0.0.1:8000 adresinde çalışır.

# Kullanım
URL Kısaltma:
POST isteği ile /shorten/ endpoint'ine uzun bir URL gönderilir ve kısaltılmış URL yanıt olarak alınır:

bash
Copy code
curl -X 'POST' \
  'http://127.0.0.1:8000/shorten/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'url=https://www.example.com'
Kısaltılmış URL'ye Erişim:
Kısaltılmış URL'ye gidildiğinde, otomatik olarak orijinal URL'ye yönlendirilirsiniz.

# Testler
Uygulamanın doğru çalıştığından emin olmak için entegre testleri çalıştırın:

bash
Copy code
pytest test_main.py

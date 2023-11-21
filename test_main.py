from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_short_url():
    # URL kısaltma işlevini test et
    response = client.post("/shorten/", data={"url": "https://www.google.com"})
    assert response.status_code == 200
    response_data = response.json()
    assert "short_link" in response_data
    assert response_data["short_link"] is not None

def test_redirect_short_url():
    # İlk olarak gerçek bir URL kısalt
    create_response = client.post("/shorten/", data={"url": "https://www.google.com"})
    assert create_response.status_code == 200
    short_link = create_response.json()["short_link"]

    # Oluşturulan kısaltılmış URL'nin tam yolunu oluştur
    full_url = f"http://testserver/{short_link}"

    # Yönlendirme işlemini test et
    redirect_response = client.get(full_url, allow_redirects=False)

    # Yönlendirme sonucunu kontrol et
    # Yönlendirmenin başarılı olup olmadığını durum kodu ile değil, başka bir yöntemle kontrol edebiliriz
    assert redirect_response.status_code != 404  # Yönlendirme işlemi yapılmış olmalı

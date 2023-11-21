from fastapi import FastAPI, HTTPException, Form
from fastapi.responses import RedirectResponse  # Bu satırı ekleyin
from pydantic import BaseModel, HttpUrl
import sqlite3
import random
import string


app = FastAPI()

# SQLite veritabanı bağlantısı için yardımcı fonksiyon
def get_db_connection():
    conn = sqlite3.connect('urls.db', check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

# Rastgele kısa link oluşturmak için fonksiyon
def generate_short_link():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

# Uygulama başlatıldığında veritabanı tablosunu oluştur
@app.on_event("startup")
async def startup():
    conn = get_db_connection()
    conn.execute("CREATE TABLE IF NOT EXISTS urls (id INTEGER PRIMARY KEY, original_url TEXT, short_link TEXT UNIQUE)")
    conn.close()

# URL kısaltma işlemi için endpoint
@app.post("/shorten/")
def create_short_url(url: HttpUrl = Form(...)):
    short_link = generate_short_link()
    conn = get_db_connection()
    # url objesinin içindeki string URL'yi almak için str(url) kullanılır
    conn.execute("INSERT INTO urls (original_url, short_link) VALUES (?, ?)", (str(url), short_link))
    conn.commit()
    conn.close()
    return {"short_link": short_link}


# Kısaltılmış URL yönlendirmesi için endpoint
@app.get("/{short_link}")
def redirect_short_url(short_link: str):
    conn = get_db_connection()
    url_data = conn.execute("SELECT original_url FROM urls WHERE short_link = ?", (short_link,)).fetchone()
    conn.close()
    if url_data:
        return RedirectResponse(url=url_data["original_url"])
    raise HTTPException(status_code=404, detail="URL not found")


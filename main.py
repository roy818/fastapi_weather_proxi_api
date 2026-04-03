from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import requests

from database import SessionLocal, engine, Base
from models import WeatherLog
from schemas import WeatherCreate
from crud import save_weather

Base.metadata.create_all(bind=engine)

app = FastAPI()

API_KEY = "09b4ba8a4129242026c72b7f15a083fd"

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/weather")
def get_weather(data: WeatherCreate, db: Session = Depends(get_db)):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={data.city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="City not found")

    result = response.json()

    temp = result["main"]["temp"]
    desc = result["weather"][0]["description"]

    saved = save_weather(db, data.city, temp, desc)

    return {
        "city": saved.city,
        "temperature": saved.temperature,
        "description": saved.description
    }

@app.get("/history")
def history(db: Session = Depends(get_db)):
    return db.query(WeatherLog).all()

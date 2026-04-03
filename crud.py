from sqlalchemy.orm import Session
from models import WeatherLog

def save_weather(db: Session, city: str, temp: float, desc: str):
    record = WeatherLog(city=city, temperature=temp, description=desc)
    db.add(record)
    db.commit()
    db.refresh(record)
    return record

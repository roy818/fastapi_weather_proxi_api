from sqlalchemy import Column, Integer, String, Float
from database import Base

class WeatherLog(Base):
    __tablename__ = "weather_logs"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, index=True)
    temperature = Column(Float)
    description = Column(String)

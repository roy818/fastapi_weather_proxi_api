from pydantic import BaseModel

class WeatherCreate(BaseModel):
    city: str

class WeatherResponse(BaseModel):
    city: str
    temperature: float
    description: str

    class Config:
        orm_mode = True

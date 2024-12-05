from datetime import datetime

from pydantic import BaseModel


class Measurement(BaseModel):
    temperature: float  # metric °C
    humidity: int  # %
    pressure: int  # hPa
    sunrise: datetime
    sunset: datetime
    country: str
    city: str
    dt: datetime

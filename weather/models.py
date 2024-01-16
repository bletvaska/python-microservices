from datetime import datetime

from pydantic import BaseModel


class Measurement(BaseModel):
    dt: datetime            # UTC
    temperature: float      # °C
    humidity: float
    pressure: float         # hPa
    city: str
    country: str
    wind_speed: float       # m/s
    wind_direction: int     # °
    sunrise: datetime       # UTC
    sunset: datetime        # UTC
    icon: str

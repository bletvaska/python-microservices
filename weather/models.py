from datetime import datetime

from sqlmodel import SQLModel, Field


class Measurement(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
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

from datetime import datetime

from sqladmin import ModelView
from sqlmodel import SQLModel, Field


class Measurement(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    temperature: float  # metric °C
    humidity: int  # %
    pressure: int  # hPa
    sunrise: datetime
    sunset: datetime
    country: str
    city: str
    dt: datetime


class MeasurementAdmin(ModelView, model=Measurement):
    pass

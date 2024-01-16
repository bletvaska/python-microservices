from datetime import datetime

from sqladmin import ModelView
from sqlmodel import SQLModel, Field


class Measurement(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    dt: datetime  # UTC
    temperature: float  # °C
    humidity: float
    pressure: float  # hPa
    city: str
    country: str
    wind_speed: float  # m/s
    wind_direction: int  # °
    sunrise: datetime  # UTC
    sunset: datetime  # UTC
    icon: str


class MeasurementAdmin(ModelView, model=Measurement):
    column_list = [
        Measurement.id,
        Measurement.dt,
        Measurement.city,
        Measurement.temperature,
        Measurement.humidity,
        Measurement.pressure,
        Measurement.sunrise,
        Measurement.sunset,
    ]
    icon = "fa-solid fa-temperature-half"
    column_searchable_list = [
        Measurement.city,
        Measurement.country
    ]
    column_sortable_list = [
        Measurement.dt,
        Measurement.temperature,
        Measurement.humidity,
        Measurement.pressure,
    ]
    page_size = 50
    page_size_options = [25, 50, 100, 200]

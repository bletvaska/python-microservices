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
    icon = 'fa-solid fa-temperature-half'
    column_list = [
        Measurement.id,
        Measurement.dt,
        Measurement.city,
        Measurement.temperature,
        Measurement.humidity,
        Measurement.pressure,
    ]
    column_labels = {
        Measurement.dt: 'Measurement Time'
    }
    column_sortable_list = [
        Measurement.dt,
        Measurement.city
    ]
    column_searchable_list = [
        Measurement.city,
        Measurement.country,
    ]
    page_size = 50
    page_size_options = [25, 50, 100]

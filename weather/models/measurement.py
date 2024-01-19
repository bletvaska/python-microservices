from datetime import datetime
from typing import Any

from pydantic import BaseModel, HttpUrl, field_validator, model_validator
from sqladmin import ModelView
from sqlmodel import SQLModel, Field

from weather.dependencies import get_settings


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


class MeasurementOut(BaseModel):
    city: str
    temperature: float
    url: HttpUrl | None = None

    # @model_validator(mode='before')
    # # @classmethod
    # def double(self, data: Any) -> Any:
    #     # print(data)
    #     # print(type(data))
    #     print(self)
    #
    #     # if isinstance(data, dict):
    #     self.url = f'{get_settings().base_url}/api/measurement/{self.id}'
    #
    #     return self


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
    column_labels = {
        Measurement.dt: 'Measurement Time'
    }

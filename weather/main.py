#!/usr/bin/env python3
import http

import pendulum
from loguru import logger
import uvicorn
from fastapi import FastAPI
import httpx
from fastapi_restful.tasks import repeat_every
from sqladmin import Admin
from sqlmodel import create_engine, SQLModel, Session

from weather.api.measurements import router as measurements_router
from weather.models.measurement import Measurement, MeasurementAdmin
from weather.models.settings import Settings

app = FastAPI()
app.include_router(measurements_router)

settings = Settings()

# create db schema
engine = create_engine(settings.db_uri)
SQLModel.metadata.create_all(engine)

# admin ui
admin = Admin(app, engine)
admin.add_view(MeasurementAdmin)


@app.on_event("startup")
@repeat_every(seconds=20 * 60)
def retrieve_weather_data():
    logger.info('Retrieving weather data.')

    params = {
        'q': 'kosice',
        'units': 'metric',
        'appid': settings.api_token,
        'lang': 'en'
    }
    response = httpx.get('https://api.openweathermap.org/data/2.5/weather', params=params)

    if response.status_code == http.HTTPStatus.OK:
        data = response.json()
        measurement = Measurement(
            dt=pendulum.from_timestamp(data['dt']),
            temperature=data['main']['temp'],
            humidity=data['main']['humidity'],
            pressure=data['main']['pressure'],
            sunrise=pendulum.from_timestamp(data['sys']['sunrise']),
            sunset=pendulum.from_timestamp(data['sys']['sunset']),
            country=data['sys']['country'],
            city=data['name'],
            wind_speed=data['wind']['speed'],
            wind_direction=data['wind']['deg'],
            icon=data['weather'][0]['icon']
        )

        engine = create_engine(settings.db_uri)
        with Session(engine) as session:
            session.add(measurement)
            session.commit()

        logger.info('Measurement successfully stored.')

    else:
        logger.error(f'Data were not retrieved correctly. HTTP status code is {response.status_code}.')


def main():
    # run service
    uvicorn.run('weather.main:app', reload=True, host='127.0.0.1', port=8000)


if __name__ == '__main__':
    main()

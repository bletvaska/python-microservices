import http

import httpx
import pendulum
from fastapi import APIRouter
from fastapi_restful.tasks import repeat_every
from loguru import logger
from sqlmodel import create_engine, Session

from weather.dependencies import get_settings
from weather.models.measurement import Measurement
from weather.models.settings import Settings

router = APIRouter()


@router.on_event("startup")
@repeat_every(seconds=20 * 60)
def retrieve_weather_data():
    logger.info('Retrieving weather data.')

    params = {
        'q': 'kosice',
        'units': 'metric',
        'appid': get_settings().api_token,
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

        engine = create_engine(get_settings().db_uri)
        with Session(engine) as session:
            session.add(measurement)
            session.commit()

        logger.info('Measurement successfully stored.')

    else:
        logger.error(f'Data were not retrieved correctly. HTTP status code is {response.status_code}.')

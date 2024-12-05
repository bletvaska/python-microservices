from contextlib import asynccontextmanager
from http import HTTPStatus
from typing import Literal

import httpx
from fastapi import FastAPI, HTTPException

from .dependencies import get_settings
from .models.measurement import Measurement


@asynccontextmanager
async def lifespan(app: FastAPI):
    # setup
    print('>> App Initialization')

    yield

    # teardown
    print('>> App Shutdown')

app = FastAPI(lifespan=lifespan)


@app.get('/api/weather', description='get weather info for given city')
async def get_weather(city: str, units: Literal['standard', 'metric', 'imperial'] = 'metric'):
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'units': units,
        'appid': get_settings().api_token
    }
    response = httpx.get(url, params=params)
    data = response.json()

    measurement = Measurement(
        dt = data['dt'],
        city = data['name'],
        country = data['sys']['country'],
        temperature = data['main']['temp'],
        humidity = data['main']['humidity'],
        pressure = data['main']['pressure'],
        sunrise = data['sys']['sunrise'],
        sunset = data['sys']['sunset'],
    )

    if response.status_code != HTTPStatus.OK:
        raise HTTPException(response.status_code, detail={
            'message': data['message'],
        })

    return measurement


def weather_scraper():
    # scrape data
    # create measurement
    # store measurement to db
    pass

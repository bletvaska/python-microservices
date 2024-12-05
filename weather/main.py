from contextlib import asynccontextmanager
from http import HTTPStatus
from typing import Literal

import httpx
from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import FastAPI, HTTPException

from .dependencies import get_settings, get_db_engine
from .models.measurement import Measurement


def scrape_data():
    print('>> scraping data')

    # scrape data
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': 'kosice',
        'units': 'metric',
        'appid': get_settings().api_token
    }
    response = httpx.get(url, params=params)
    data = response.json()

    # create measurement
    measurement = Measurement(
        dt=data['dt'],
        city=data['name'],
        country=data['sys']['country'],
        temperature=data['main']['temp'],
        humidity=data['main']['humidity'],
        pressure=data['main']['pressure'],
        sunrise=data['sys']['sunrise'],
        sunset=data['sys']['sunset'],
    )
    print(measurement)

    # store measurement to db
    engine = get_db_engine()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # setup
    print('>> App Initialization')

    # start scheduler
    scheduler = BackgroundScheduler()
    scheduler.add_job(scrape_data, 'interval', seconds=get_settings().interval)
    scheduler.start()

    yield

    # teardown
    print('>> App Shutdown')
    scheduler.shutdown()


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
        dt=data['dt'],
        city=data['name'],
        country=data['sys']['country'],
        temperature=data['main']['temp'],
        humidity=data['main']['humidity'],
        pressure=data['main']['pressure'],
        sunrise=data['sys']['sunrise'],
        sunset=data['sys']['sunset'],
    )

    if response.status_code != HTTPStatus.OK:
        raise HTTPException(response.status_code, detail={
            'message': data['message'],
        })

    return measurement

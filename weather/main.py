from contextlib import asynccontextmanager
from http import HTTPStatus
from typing import Literal, Annotated

import httpx
import pendulum
from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import FastAPI, HTTPException, Depends
from sqladmin import Admin
from sqlmodel import SQLModel, Session, select

from .dependencies import get_settings, get_db_engine, get_db_session
from .models.measurement import Measurement, MeasurementAdmin


def scrape_data():
    print('>> scraping data')

    # scrape data
    settings = get_settings()
    url = 'https://api.openweathermap.org/data/2.5/weather'

    for city in settings.cities:
        params = {
            'q': city,
            'units': 'metric',
            'appid': settings.api_token
        }
        response = httpx.get(url, params=params)
        data = response.json()

        # create measurement
        measurement = Measurement(
            dt=pendulum.from_timestamp(data['dt']),
            city=data['name'],
            country=data['sys']['country'],
            temperature=data['main']['temp'],
            humidity=data['main']['humidity'],
            pressure=data['main']['pressure'],
            sunrise=pendulum.from_timestamp(data['sys']['sunrise']),
            sunset=pendulum.from_timestamp(data['sys']['sunset']),
        )
        print(measurement)

        # store measurement to db
        with Session(get_db_engine()) as session:
            session.add(measurement)  # INSERT
            session.commit()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # setup
    print('>> App Initialization')
    # scrape_data()

    # start scheduler
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        scrape_data,
        'interval',
        seconds=get_settings().interval)
    scheduler.start()

    yield

    # teardown
    print('>> App Shutdown')
    scheduler.shutdown()


app = FastAPI(lifespan=lifespan)
print(get_settings())

# create db schema
SQLModel.metadata.create_all(get_db_engine())

# create admin view
admin = Admin(app, get_db_engine())
admin.add_view(MeasurementAdmin)


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
        dt=pendulum.from_timestamp(data['dt']),
        city=data['name'],
        country=data['sys']['country'],
        temperature=data['main']['temp'],
        humidity=data['main']['humidity'],
        pressure=data['main']['pressure'],
        sunrise=pendulum.from_timestamp(data['sys']['sunrise']),
        sunset=pendulum.from_timestamp(data['sys']['sunset']),
    )

    session = Session(get_db_engine())
    # from IPython import embed; embed()
    session.add(measurement)  # INSERT
    session.commit()
    session.close()

    if response.status_code != HTTPStatus.OK:
        raise HTTPException(response.status_code, detail={
            'message': data['message'],
        })

    return measurement


@app.get('/api/measurements')
async def get_measurements(session: Annotated[Session, Depends(get_db_session)]):
    # SELECT * FROM measurement
    statement = select(Measurement)
    return session.exec(statement).all()

from contextlib import asynccontextmanager

import httpx
import pendulum
from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import FastAPI
from sqladmin import Admin
from sqlmodel import SQLModel, Session

from .dependencies import get_settings, get_db_engine
from .models.measurement import Measurement, MeasurementAdmin
from .routers import measurements


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
app.include_router(
    measurements.router,
    prefix='/api/measurements',
)
# print(get_settings())

# create db schema
SQLModel.metadata.create_all(get_db_engine())

# create admin view
admin = Admin(app, get_db_engine())
admin.add_view(MeasurementAdmin)

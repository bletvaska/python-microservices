#!/usr/bin/env python3
from pathlib import Path

import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi_pagination import add_pagination
from loguru import logger
from sqladmin import Admin
from sqlmodel import create_engine, SQLModel

from weather.api.healthcheck import router as healthcheck_router
from weather.api.measurements import router as measurements_router
from weather.cron import router as cron_router
from weather.dependencies import get_settings
from weather.models.measurement import MeasurementAdmin
from weather.views.homepage import router as homepage_router

app = FastAPI()
app.include_router(measurements_router)
app.include_router(cron_router)
app.include_router(homepage_router)
app.include_router(healthcheck_router)

add_pagination(app)

app.mount(
    '/static',
    StaticFiles(directory=Path(__file__).parent / 'static'),
    name='static'
)

# create db schema
engine = create_engine(get_settings().db_uri)
SQLModel.metadata.create_all(engine)

# admin ui
admin = Admin(app, engine)
admin.add_view(MeasurementAdmin)


@app.on_event('startup')
def on_start():
    logger.info('Application is starting.')

    # with next(get_session()) as session:
    #     statement = select(Measurement)
    #     measurement = session.exec(statement).all()[0]
    #     data = measurement.model_dump()
    #     print(MeasurementOut(**data))


def main():
    uvicorn.run(
        'weather.main:app',
        reload=True,
        host='127.0.0.1',
        port=8000,
        log_level='error'
    )


if __name__ == '__main__':
    main()

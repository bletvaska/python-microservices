#!/usr/bin/env python3

import uvicorn
from fastapi import FastAPI
from fastapi_pagination import add_pagination
from sqladmin import Admin
from sqlmodel import create_engine, SQLModel
from loguru import logger

from weather.api.measurements import router as measurements_router
from weather.cron import router as cron_router
from weather.dependencies import get_settings
from weather.models.measurement import MeasurementAdmin

app = FastAPI()
app.include_router(measurements_router)
app.include_router(cron_router)

add_pagination(app)

# create db schema
engine = create_engine(get_settings().db_uri)
SQLModel.metadata.create_all(engine)

# admin ui
admin = Admin(app, engine)
admin.add_view(MeasurementAdmin)


@app.on_event('startup')
def on_start():
    logger.info('Application is starting.')


def main():
    uvicorn.run('weather.main:app', reload=True, host='127.0.0.1', port=8000, log_level='error')


if __name__ == '__main__':
    main()

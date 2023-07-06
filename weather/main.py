#!/usr/bin/env python
from pathlib import Path

import uvicorn as uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi_pagination import add_pagination
from sqladmin import Admin
from sqlmodel import create_engine

from weather.dependencies import get_settings
from weather.models.pokemon import PokemonAdmin
from weather.api.weather import router as weather_router
from weather.views.dashboard import router as dashboard_router

app = FastAPI()


def initialize():
    app.mount('/static',
              StaticFiles(directory=Path(__file__).parent / 'static'),
              name='static')

    # routes
    app.include_router(weather_router)
    app.include_router(dashboard_router)
    add_pagination(app)

    # sql admin
    admin = Admin(app, create_engine(get_settings().db_uri))
    admin.add_view(PokemonAdmin)


if __name__ == '__main__':
    initialize()
    uvicorn.run('weather.main:app', reload=True, host='0.0.0.0', port=8000)
else:
    # when running from cli only: uviconr weather.main:app
    initialize()

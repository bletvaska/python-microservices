#!/usr/bin/env python
from pathlib import Path
from time import sleep

import uvicorn as uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi_pagination import add_pagination
from sqladmin import Admin
from sqlmodel import create_engine
from starlette.middleware.base import BaseHTTPMiddleware

from pokedex.api.pokemons import router as pokemons_router
from pokedex.dependencies import get_settings
from pokedex.middleware import add_process_time_to_header
from pokedex.models.pokemon import PokemonAdmin
from pokedex.views.homepage import router as homepage_router
from pokedex.views.pokemon_list import router as pokemon_list_router
from pokedex.views.pokemon_detail import router as pokemon_detail_router
from pokedex.api.healthcheck import router as healthcheck_router

app = FastAPI()
app.mount('/static',
          StaticFiles(directory=Path(__file__).parent / 'static'),
          name='static')

# middleware
app.add_middleware(BaseHTTPMiddleware, dispatch=add_process_time_to_header)

# routes
app.include_router(pokemons_router)
app.include_router(homepage_router)
app.include_router(pokemon_list_router)
app.include_router(pokemon_detail_router)
app.include_router(healthcheck_router)
add_pagination(app)

# sql admin
admin = Admin(app, create_engine(get_settings().db_uri))
admin.add_view(PokemonAdmin)


@app.get('/deadlock')
def deadlock():
    while True:
        print('>> working')
        sleep(1)


if __name__ == '__main__':
    uvicorn.run('pokedex.main:app', reload=True, host='0.0.0.0', port=8000)

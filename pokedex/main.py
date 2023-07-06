#!/usr/bin/env python
from pathlib import Path

import uvicorn as uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi_pagination import add_pagination
from sqladmin import Admin
from sqlmodel import create_engine

from pokedex.api.pokemons import router as pokemons_router
from pokedex.dependencies import get_settings
from pokedex.models.pokemon import PokemonAdmin
from pokedex.views.homepage import router as homepage_router
from pokedex.views.list_pokemons import router as list_pokemons_router

app = FastAPI()
app.mount('/static',
          StaticFiles(directory=Path(__file__).parent / 'static'),
          name='static')

# routes
app.include_router(pokemons_router)
app.include_router(homepage_router)
app.include_router(list_pokemons_router)
add_pagination(app)

# sql admin
admin = Admin(app, create_engine(get_settings().db_uri))
admin.add_view(PokemonAdmin)

if __name__ == '__main__':
    uvicorn.run('pokedex.main:app', reload=True, host='0.0.0.0', port=8000)

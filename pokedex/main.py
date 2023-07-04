#!/usr/bin/env python

import uvicorn as uvicorn
from fastapi import FastAPI
from fastapi_pagination import add_pagination
from sqladmin import Admin
from sqlmodel import create_engine

from pokedex.api.pokemons import router as pokemons_router
from pokedex.dependencies import get_settings
from pokedex.models.pokemon import PokemonAdmin

app = FastAPI()
app.include_router(pokemons_router)
add_pagination(app)

# db engine
engine = create_engine(get_settings().db_uri)
admin = Admin(app, engine)
admin.add_view(PokemonAdmin)

if __name__ == '__main__':
    uvicorn.run('pokedex.main:app', reload=True, host='0.0.0.0', port=8000)

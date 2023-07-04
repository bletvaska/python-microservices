import math

import uvicorn as uvicorn
from fastapi import FastAPI, HTTPException
from sqladmin import Admin
from sqlmodel import create_engine, Session, select

from pokedex.api.pokemons import router as pokemons_router
from pokedex.dependencies import get_settings
from pokedex.models.pokemon import PokemonAdmin, Pokemon

app = FastAPI()
app.include_router(pokemons_router)

# db engine
engine = create_engine(get_settings().db_uri)
# 'sqlite:////home/mirek/Documents/kurzy/python-courses/python-microservices/resources/pokedex.sqlite'
admin = Admin(app, engine)
admin.add_view(PokemonAdmin)

if __name__ == '__main__':
    uvicorn.run('pokedex.main:app', reload=True, host='0.0.0.0', port=8000)

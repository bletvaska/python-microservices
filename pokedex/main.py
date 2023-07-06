#!/usr/bin/env python

import uvicorn as uvicorn
from fastapi import FastAPI, Request
from fastapi_pagination import add_pagination
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqladmin import Admin
from sqlmodel import create_engine

from pokedex.api.pokemons import router as pokemons_router
from pokedex.dependencies import get_settings
from pokedex.models.pokemon import PokemonAdmin

app = FastAPI()
app.include_router(pokemons_router)
add_pagination(app)
app.mount('/static', StaticFiles(directory='pokedex/static'), name='static')
templates = Jinja2Templates(directory='pokedex/templates/')

# db engine
engine = create_engine(get_settings().db_uri)
admin = Admin(app, engine)
admin.add_view(PokemonAdmin)


@app.get('/', response_class=HTMLResponse)
def homepage(request: Request):
    context = {
        'request': request,
        'title': 'Pokédex',
    }
    return templates.TemplateResponse('home.tpl.html', context)


if __name__ == '__main__':
    uvicorn.run('pokedex.main:app', reload=True, host='0.0.0.0', port=8000)

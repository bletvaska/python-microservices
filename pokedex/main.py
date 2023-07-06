#!/usr/bin/env python

import uvicorn as uvicorn
from fastapi import FastAPI, Request, Depends
from fastapi_pagination import add_pagination
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqladmin import Admin
from sqlmodel import create_engine, select, Session

from pokedex.api.pokemons import router as pokemons_router
from pokedex.dependencies import get_settings, get_session
from pokedex.models.pokemon import PokemonAdmin, Pokemon

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
        'title': 'Vitajte | Pokédex',
    }
    return templates.TemplateResponse('home.tpl.html', context)


@app.get('/pokedex', response_class=HTMLResponse)
def view_list_of_pokemons(request: Request,
                          page_size: int = 20,
                          offset: int = 0,
                          session: Session = Depends(get_session)):
    statement = select(Pokemon).offset(page_size * offset).limit(page_size)
    pokemons = session.exec(statement).all()

    context = {
        'request': request,
        'title': 'Všetci Pokémoni na jednom mieste | Pokédex',
        'pokemons': pokemons,
        'offset': offset,
        'page_size': page_size
    }

    return templates.TemplateResponse('pokemon-list.tpl.html', context)


if __name__ == '__main__':
    uvicorn.run('pokedex.main:app', reload=True, host='0.0.0.0', port=8000)

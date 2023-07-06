from fastapi import Request, Depends, APIRouter
from fastapi.responses import HTMLResponse
from sqlmodel import Session, select
from fastapi.templating import Jinja2Templates

from weather.dependencies import get_session, get_jinja
from weather.models.pokemon import Pokemon

router = APIRouter()


@router.get('/pokedex/{pokedex_number}', response_class=HTMLResponse)
def pokemon_detail(request: Request, pokedex_number: int,
                   session: Session = Depends(get_session),
                   jinja: Jinja2Templates = Depends(get_jinja)):
    statement = select(Pokemon).where(Pokemon.pokedex_number == pokedex_number)
    pokemon = session.exec(statement).one_or_none()

    context = {
        'request': request,
        'title': f'{pokemon.name} | Pokédex',
        'pokemon': pokemon,
    }

    return jinja.TemplateResponse('pokemon-detail.tpl.html', context)

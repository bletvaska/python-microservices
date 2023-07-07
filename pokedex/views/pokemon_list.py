from fastapi import Request, Depends, APIRouter
from fastapi.responses import HTMLResponse
from sqlmodel import Session, select, or_
from fastapi.templating import Jinja2Templates

from pokedex.dependencies import get_session, get_jinja
from pokedex.models.pokemon import Pokemon

router = APIRouter()


@router.get('/pokedex', response_class=HTMLResponse)
def view_list_of_pokemons(request: Request,
                          page_size: int = 20,
                          offset: int = 0,
                          query: str | None = None,
                          session: Session = Depends(get_session),
                          jinja: Jinja2Templates = Depends(get_jinja)):

    statement = select(Pokemon).offset(page_size * offset).limit(page_size)
    if query is not None:
        statement = statement.where(or_(
            Pokemon.name.ilike(f'%{query}%'),
            Pokemon.pokedex_number == query
        ))

    pokemons = session.exec(statement).all()

    context = {
        'request': request,
        'title': 'Všetci Pokémoni na jednom mieste | Pokédex',
        'pokemons': pokemons,
        'offset': offset,
        'page_size': page_size
    }

    return jinja.TemplateResponse('pokemon-list.tpl.html', context)

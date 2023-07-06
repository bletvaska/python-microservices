import fastapi
from fastapi import HTTPException, Depends, Form
from fastapi_pagination.links import LimitOffsetPage
from fastapi_pagination.ext.sqlmodel import paginate
from sqlmodel import Session, select

from pokedex.dependencies import get_session
from pokedex.models.pokemon import Pokemon

router = fastapi.APIRouter()


@router.get('/api/pokemons', response_model=LimitOffsetPage[Pokemon])
def get_list_of_pokemons(classification: str = None,
                         session: Session = Depends(get_session)):
    statement = select(Pokemon)

    if classification is not None:
        statement = statement.where(Pokemon.classification == classification)

    return paginate(session, statement)


@router.get('/api/pokemons/{pokedex_number}')
def get_pokemon_detail(pokedex_number: int,
                       session: Session = Depends(get_session)):
    return _get_pokemon_by_id(pokedex_number, session)


@router.patch('/api/pokemons/{pokedex_number}')
def partial_update_pokemon(pokedex_number: int,
                           name: str = Form(None),
                           weight: float = Form(None),
                           height: float = Form(None),
                           session: Session = Depends(get_session)):
    pokemon = _get_pokemon_by_id(pokedex_number, session)

    # update pokemon with new attributes
    if name is not None:
        pokemon.name = name

    if weight is not None:
        pokemon.weight = weight

    if height is not None:
        pokemon.height = height

    # update db entry
    session.add(pokemon)
    session.commit()
    session.refresh(pokemon)

    # return
    return pokemon


def _get_pokemon_by_id(pokedex_number: int, session: Session):
    statement = select(Pokemon).where(Pokemon.pokedex_number == pokedex_number)
    pokemon = session.exec(statement).one_or_none()

    if pokemon is None:
        raise HTTPException(
            status_code=404,
            detail=f'Pokémon with pokédex number {pokedex_number} not found.',
        )

    return pokemon

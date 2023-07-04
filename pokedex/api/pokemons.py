import math

from fastapi import HTTPException
from sqlmodel import Session, select

from pokedex.models.pokemon import Pokemon


@app.get('/api/pokemons')
def get_list_of_pokemons(classification: str = None, offset: int = 0, page_size: int = 10):
    pokemons_total = 801

    with Session(engine) as session:
        statement = select(Pokemon).offset(offset * page_size).limit(page_size)

        if classification is not None:
            statement = statement.where(Pokemon.classification == classification)

        pokemons = session.exec(statement).all()

    previous_link = None
    if offset - 1 > 0:
        previous_link = f'/api/pokemons?page_size={page_size}&offset={offset - 1}'

    return {
        'first': f'/api/pokemons?page_size={page_size}',
        'previous': previous_link,
        'next': f'/api/pokemons?page_size={page_size}&offset={offset + 1}',
        'last': f'/api/pokemons?page_size={page_size}&offset={math.ceil(pokemons_total / page_size)}',
        'results': pokemons
    }


@app.get('/api/pokemons/{pokedex_number}')
def get_pokemon_detail(pokedex_number: int):
    with Session(engine) as session:
        statement = select(Pokemon).where(Pokemon.pokedex_number == pokedex_number)
        pokemon = session.exec(statement).one_or_none()

        if pokemon is None:
            raise HTTPException(
                status_code=404,
                detail=f'Pokémon with pokédex number {pokedex_number} not found.',
            )

    return pokemon

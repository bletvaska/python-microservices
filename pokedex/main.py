import uvicorn as uvicorn
from fastapi import FastAPI, HTTPException
from sqladmin import Admin
from sqlmodel import create_engine, Session, select

from pokedex.models.pokemon import PokemonAdmin, Pokemon

app = FastAPI()

# db engine
engine = create_engine(
    'sqlite:////home/mirek/Documents/kurzy/python-courses/python-microservices/resources/pokedex.sqlite')
admin = Admin(app, engine)
admin.add_view(PokemonAdmin)


@app.get('/api/pokemons')
def get_list_of_pokemons():
    with Session(engine) as session:
        statement = select(Pokemon)
        pokemons = session.exec(statement).all()

    return pokemons


@app.get('/api/pokemons/{pokedex_number}')
def get_list_of_pokemons(pokedex_number: int):
    with Session(engine) as session:
        statement = select(Pokemon).where(Pokemon.pokedex_number == pokedex_number)
        pokemon = session.exec(statement).one_or_none()

        if pokemon is None:
            raise HTTPException(
                status_code=404,
                detail=f'Pokémon with pokédex number {pokedex_number} not found.',
            )

    return pokemon


@app.get('/')
def homepage():
    """
    Returns homepage.
    """
    return {
        "message": "hello world"
    }


if __name__ == '__main__':
    uvicorn.run('pokedex.main:app', reload=True, host='0.0.0.0', port=8000)

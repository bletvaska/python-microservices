# Pokemon Detail


```python
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
```


## Output Model


## Links

* [FastAPI: Response Model - Return Type](https://fastapi.tiangolo.com/tutorial/response-model/)
* 
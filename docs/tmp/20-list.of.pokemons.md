# Getting the List of Pokemons


## First Steps

zacneme tym, ze vytvorime funkciu `get_list_of_files()` v module `main.py`, ktorá vráti zoznam Pokémonov:

```python
@app.get('/api/pokemons/', summary="Get list of Pokémons.")
def list_of_pokemons():
    return []
```

## Getting the Data from DB

```python
@app.get('/api/pokemons/', summary="Get list of Pokémons.")
def list_of_pokemons():
   statement = select(Pokemon)
   session = Session(engine)
   pokemons = session.exec(statement).all()
   session.close()
   return pokemons
```


## Context Manager

```python
@app.get('/api/pokemons')
def get_list_of_pokemons():
    with Session(engine) as session:
        statement = select(Pokemon)
        pokemons = session.exec(statement).all()

    return pokemons
```

# Project Structure Refactoring

## Architektúra projektu

Pre REST API urobime samostatny balik a v nom modul files.py, ktory bude obsahovat vsetky HTTP metody pre pracu so 
subormi. Štruktúra projektu bude nasledne vyzerat takto:

```
project
├── pokedex
│   ├── api
│   │   ├── pokemons.py
│   │   └── __init__.py
│   ├── __init__.py
│   └── main.py
├── pyproject.toml
└── readme.md
```

## Module `pokemons.py`

aby vsetko pracovalo ako malo, v module main.py musime pridat tento router do objektu aplikacie app:

```python
# application init
app = FastAPI()
app.include_router(pokemons.router)
```
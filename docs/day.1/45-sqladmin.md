# SQL Admin

Ak chceme pracovať s údajmi uloženými v databáze, musíme sa k databáze pripojiť z našej aplikácie. V tomto kroku 
preto vytvoríme spojenie s databázou spolu s jednoduchým admin rozhraním z modulu SQLAlchemy Admin. 

## Instalacia

```bash
$ poetry add sqladmin
```

## Spojenie s databázou

Na začiatok súboru `main.py` vytvoríme premennú `engine`, pomocou ktorej sa budeme vedieť spojiť s databázou.

Do súboru `main.py` preto vložíme nasledovný fragment kódu:

```python
from sqlmodel import create_engine

# db engine
engine = create_engine('sqlite:///pokedex.sqlite')
```


## Vytvorenie admin rozhrania

Admin rozhranie vytvoríme veľmi jednoducho: pod riadok, v ktorom sme vytvorili objekt `engine` vytvoríme admin 
rozhranie riadkom:

```python
from sqladmin import Admin
from sqlmodel import create_engine

engine = create_engine("sqlite:///pokedex.sqlite")
admin = Admin(app, engine)
```

Ak sme postupovali správne, admin rozhranie bude dostupné v prehliadači na adrese http://localhost:8000/admin


## Pokemon Admin Model

V admin rozhraní zatiaľ nič nevidíme. Aby sme v ňom mohli vidieť Pokémonov z databázy, musíme pre ne vytvoriť 
samostatný model. Do súboru s modelmi preto vytvoríme nový model, ktorým opíšeme, čo a ako sa má v admin rozhraní zobrazovať.

Model nazveme `PokemonAdmin`, bude potomkom triedy `ModelView` a bude opisovať admin rozhranie modelu `Pokemon`. Kód 
bude vyzerať napríklad takto:

```python
from sqladmin import ModelView

class PokemonAdmin(ModelView, model=Pokemon):
    page_size = 20
    icon = "fa-solid fa-spaghetti-monster-flying"
    column_searchable_list = [Pokemon.name]
    column_sortable_list = [Pokemon.name, Pokemon.classification, Pokemon.type1, Pokemon.type2]
    column_list = [
        Pokemon.pokedex_number,
        Pokemon.name,
        Pokemon.classification,
        Pokemon.type1,
        Pokemon.type2
    ]
```

Aby všetko fungovalo, potrebujeme admin model pridať do aplikácie:

```python
from models import PokemonAdmin

engine = create_engine("sqlite:///pokedex.sqlite")
admin = Admin(app, engine)
admin.add_view(PokemonAdmin)
```


## Linky

* [SQLAlchemy Admin](https://github.com/aminalaee/sqladmin) - projekt na Github-e
* [SQLAlchemy Admin Documentation](https://aminalaee.dev/sqladmin/) - dokumentacia modulu

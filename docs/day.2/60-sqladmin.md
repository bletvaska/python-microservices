# SQL Admin

Ak chceme pracovať s údajmi uloženými v databáze, musíme sa k databáze pripojiť z našej aplikácie. V tomto kroku
preto vytvoríme spojenie s databázou spolu s jednoduchým admin rozhraním z modulu SQLAlchemy Admin.


## Inštalácia

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


## Measurement Admin Model

V admin rozhraní zatiaľ nič nevidíme. Aby sme v ňom mohli vidieť merania z databázy, musíme pre ne vytvoriť
samostatný model. Do súboru s modelmi preto vytvoríme nový model, ktorým opíšeme, čo a ako sa má v admin rozhraní zobrazovať.

Model nazveme `MeasurementAdmin`, bude potomkom triedy `ModelView` a bude opisovať admin rozhranie modelu `Measurement`. Kód
bude vyzerať napríklad takto:

```python
class MeasurementAdmin(ModelView, model=Measurement):
    column_list = [
        Measurement.id,
        Measurement.dt,
        Measurement.city,
        Measurement.temperature,
        Measurement.humidity,
        Measurement.pressure,
        Measurement.sunrise,
        Measurement.sunset,
    ]
    icon = "fa-solid fa-temperature-half"
    column_searchable_list = [
        Measurement.city,
        Measurement.country
    ]
    column_sortable_list = [
        Measurement.dt,
        Measurement.temperature,
        Measurement.humidity,
        Measurement.pressure,
    ]
    page_size = 50
    page_size_options = [25, 50, 100, 200]
    column_labels = {
        Measurement.dt: 'Measurement Time'
    }
```

Aby všetko fungovalo, potrebujeme admin model pridať do aplikácie:

```python
from models import MeasurementAdmin

engine = create_engine("sqlite:///database.sqlite")
admin = Admin(app, engine)
admin.add_view(MeasurementAdmin)
```


## Linky

* [SQLAlchemy Admin](https://github.com/aminalaee/sqladmin) - projekt na Github-e
* [SQLAlchemy Admin Documentation](https://aminalaee.dev/sqladmin/) - dokumentacia modulu

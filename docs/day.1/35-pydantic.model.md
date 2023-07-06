# Pydantic Model

![Pydantic Logo](https://pydantic.dev/imgs/social.png)

[Pydantic](https://docs.pydantic.dev/latest/) is the most widely used data validation library for Python.

Balík `pydantic` najprv nainštalujeme:

```bash
$ poetry add pydantic
```
a pre lepsiu pracu si nainstalujeme aj plugin pre pycharm, aby isiel `pydantic`. otvorime nastavenia cez `File > 
Settings > Plugins` a nechame vyhladat a nainstalovat plugin s nazvom `Pydantic`.


## Výsledný model

Model pre reprezentáciu Pokémona môže vyzerať takto:

```python
from pydantic import BaseModel

class Pokemon(BaseModel):
    pokedex_number: int
    name: str
    classification: str
    type1: str
    type2: str | None
    weight: float
    height: float 
```


## Otestovanie vytvoreného modelu

Na základe vytvoreného modelu môžeme vytvoriť Pokémona:

```python
from weather.models.pokemon import Pokemon

pokemon = Pokemon(
    name='Pikachu',
    classification='Mouse Pokémon',
    type1='electric',
    type2=None,
    weight=6.0,
    height=0.4
)
```

Pristupovať k jednotlivým položkám Pokémona môžeme následne pomocou operátora `.` nasledovne:

```python
>>> pokemon.name
'Pikachu'
>>> pokemon.weight
6.0
```
# Pager

Stránkovanie výsledkov

## V čom je problém

Nemôžeme vracať všetky záznamy

* príliš veľa
* s pribúdajúcim počtom bude aj ich spracovanie a vrátenie trvať dlhší a dlhší čas
* množstvo získaných dát bude rásť s pribúdajúcim počtom položiek
* veľmi jednoducho by sme vedeli zabezpečiť DOS útok


## Stránkovanie v rámci Django

```json
{
    "count": 4321,
    "next": "http://app.com/users/?page=2",
    "previous": null,
    "results": [
        ...
    ]
}
```


## Využitie rozšírenia

Na implementáciu stránkovania použijeme modul [`fastapi-pagination`](https://uriyyo-fastapi-pagination.netlify.app). 
Najprv ho teda nainštalujeme:

```bash
$ poetry add fastapi-pagination
```

Rozšírenie ponúka viacero spôsobov, ako pracovať so stránkovaním, ako napr.:

* číslované stránkovanie - stránkovanie bude obsahovať len číselné odkazy na jednotlivé stránky 
* obmedzenie veľkosti a ofset-u stránky - je možné nastaviť, aká veľká stránka má byť a s akým odstupom začať 
  stránkovať
* stránkovanie s odkazmi - stránkovanie s odkazmi na nasledujúcu, predchádzajúcu, prvú, poslednú a aktuálnu stránku


## Code Update

Použijeme stránkovanie s odkazmi a adekvátne upravíme kód funkcie `get_list_of_pokemons()`.

Najprv upravíme typ modelu odpovede v dekorátori funkcie. Použijeme `LimitOffsetPage`:

```python
from fastapi_pagination.links import LimitOffsetPage
@router.get('/api/pokemons', response_model=LimitOffsetPage[Pokemon])
```

Keďže používame ORM, potrebujeme použiť správnu funkciu `paginate()` pre naše ORM. V našom prípade, keďže používame 
_SQLModel_, importujeme funkciu `paginate()` nasledovne:

```python
from fastapi_pagination.ext.sqlmodel import paginate
```

Následne upravíme kód funkcie a zavoláme funkciu `paginate()`. Jej parametrom je objekt sedenia databázy a príkaz na 
vykonanie SQL dopytu.

```python
from fastapi_pagination.links import LimitOffsetPage
from fastapi_pagination.ext.sqlmodel import paginate

@router.get('/api/pokemons', response_model=LimitOffsetPage[Pokemon])
def list(classification: str = None,
         session: Session = Depends(get_session)):
    statement = select(Pokemon)

    if classification is not None:
        statement = statement.where(Pokemon.classification == classification)

    return paginate(session, statement)
```

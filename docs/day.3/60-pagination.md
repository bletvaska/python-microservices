# Stránkovanie výsledkov

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

## Vlastná implementácia

najprv upravíme funkciu pre získanie všetkých meraní. pridáme do jej parametrov požiadavky dva:

* číslo stránky, a
* počet záznamov na stránke

```python
@router.get("/api/measurements")
def list_of_measurements(page: int = 1,
                         page_size: int = 20,
                         session: Session = Depends(get_session)):
```

následne upravíme dopyt:

```python
statement = (
   select(Measurement)
   .offset((page - 1) * page_size)
   .limit(page_size)
)
results = session.exec(statement).all()
```

a pouzijeme:

```bash
$ http "http://localhost:8000/api/measurements?page=5&page_size=10"
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

Dokumentacia upozornuje, ze je potrebne objekt aplikacie `FastAPI` zabalit do volania funkcie `add_pagination()`. Takze
v module `main.py` pridame riadok:

```python
add_pagination(app)
```

Použijeme stránkovanie s odkazmi a adekvátne upravíme kód funkcie `get_list_of_pokemons()`.

Najprv upravíme typ modelu odpovede v dekorátori funkcie. Použijeme `LimitOffsetPage`:

```python
from fastapi_pagination.links import LimitOffsetPage


@router.get('/api/measurements', response_model=LimitOffsetPage[Measurement])
```

Keďže používame ORM, potrebujeme použiť správnu funkciu `paginate()` pre naše ORM. V našom prípade, keďže používame
_SQLModel_, importujeme funkciu `paginate()` nasledovne:

```python
from fastapi_pagination.ext.sqlmodel import paginate
```

Následne upravíme kód funkcie a zavoláme funkciu `paginate()`. Jej parametrom je objekt sedenia databázy a príkaz na
vykonanie SQL dopytu.

```python
from fastapi_pagination.links import Page
from fastapi_pagination.ext.sqlmodel import paginate


@router.get('/api/measurements', response_model=Page[Measurement])
def list_measurements(session: Session = Depends(get_session)):
   statement = select(Measurements)
   return paginate(session, statement)
```

Nasledne mozeme vyskusat:

```bash
$ http "http://localhost:8000/api/measurements"
```

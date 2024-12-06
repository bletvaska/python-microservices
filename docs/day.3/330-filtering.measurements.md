# Filtrovanie výsledkov

Vysledky sa filtruju pomocou parametrov poziadavky (tzv. _query parameters_).


## Filtering Measurements by the `city`

Aktualizujeme funkciu o filter, pomocou ktorého získame zoznam meraní len pre príslušné miesto.

```python
from typing import Annotated

@app.get("/api/measurements")
def list_of_measurements(city: str = None, session: Annotated[Session, Depends(get_session)]):
    statement = select(Measurement).where(Measurement.city == city)
    return session.exec(statement).all()
```

Overit spravanie je mozne z prikazoveho riadku prikazom:

```bash
$ http http://localhost:8000/api/measurements city==Kosice
```

Ak však napíšeme mesto veľkými písmenami, tak nenájde nič. Ak ho nezadáme vôbec, dokonca to všetko spadne. Upravíme teda implementáciu tak, aby to fungovalo ;)

```python
@app.get('/api/measurements')
async def get_measurements(session: Annotated[Session, Depends(get_db_session)],
                           city: str = None):
    # SELECT * FROM measurement WHERE city=':city'
    statement = select(Measurement)

    if city is not None:
        statement = statement.where(func.lower(Measurement.city) == city.lower())

    return session.exec(statement).all()
```

Overit spravanie je mozne z prikazoveho riadku týmito prikazmi:

```bash
$ http http://localhost:8000/api/measurements
$ http http://localhost:8000/api/measurements city==KoSiCe
```



# Lab: Filtrovanie podľa času

Aktualizujte funkciu `get_measurements()` tak, aby bolo možné filtrovať výsledky aj podľa času merania.

Budeme pouzivat dva parametre poziadavky navyse:

* `start_date` - odkedy
* `end_date` - dokedy

```python
@app.get("/api/measurements")
def get_measurements(start_date: date | None = None,
                     end_date: date | None = None,
                     city: str | None = None,
                     session: Session = Depends(get_session)):
    statement = select(Measurement)

    if city is not None:
        statement = statement.where(func.lower(Measurement.city) == city.lower())

    if start_date is not None:
        statement = statement.where(Measurement.dt >= start_date)

    if end_date is not None:
        statement = statement.where(Measurement.dt < end_date)

    return session.exec(statement).all()
```


## Linky

* SQLModel: [Filter Data - WHERE](https://sqlmodel.tiangolo.com/tutorial/where/)

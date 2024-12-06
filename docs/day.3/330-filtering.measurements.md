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


# Filtrovanie podla casu

Budeme pouzivat dva parametre poziadavky navyse:

* `start_date` - odkedy
* `end_date` - dokedy

```python
@router.get('/api/measurements')
def list_measurements(city: str = None, start_date: datetime = None, end_date: datetime = None,
                      session: Annotated[Session, Depends(get_session)]):
   # create select statement
   statement = select(Measurement)
   if city is not None:
      statement = statement.where(Measurement.city == city)

   # execute statement
   measurement = session.exec(statement).one_or_none()

   # ...
```


## Linky

* SQLModel: [Filter Data - WHERE](https://sqlmodel.tiangolo.com/tutorial/where/)

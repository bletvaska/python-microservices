# Filtrovanie merani

Vysledky sa filtruju pomocou parametrov poziadavky (tzv. _query parameters_).


## Filtrovanie podla mesta

Budeme pouzivat jeden query parameter `city`, do ktoreho pridame mesto:

```python
@router.get('/api/measurements')
def list_measurements(city: str = None, session: Session = Depends(get_session)):
   # create select statement
   statement = select(Measurement)
   if city is not None:
      statement = statement.where(Measurement.city == city)

   # execute statement
   measurement = session.exec(statement).one_or_none()

   # ...
```


## Filtrovanie podla casu

Budeme pouzivat dva parametre poziadavky navyse:

* `start_date` - odkedy
* `end_date` - dokedy

```python
@router.get('/api/measurements')
def list_measurements(city: str = None, start_date: datetime = None, end_date: datetime = None, session: Session = Depends(get_session)):
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

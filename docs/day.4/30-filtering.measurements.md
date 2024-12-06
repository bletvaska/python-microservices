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



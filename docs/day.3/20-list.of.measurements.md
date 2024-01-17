# Getting the List of Pokemons


## Getting the Data from DB

```python
@app.get("/api/measurements")
def list_of_measurements(city: str = None):
    engine = create_engine('sqlite:///database.sqlite')

    with Session(engine) as session:
        statement = select(Measurement)
        if city is not None:
            statement = statement.where(Measurement.city == city)

        return session.exec(statement).all()
```




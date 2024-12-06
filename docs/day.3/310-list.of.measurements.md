# Získanie zoznamu všetkých meraní

* endpoint `/api/measurements`
* metóda `GET
* vracať bude zoznam meraní`


## Getting the Data from DB

Vytvoríme funkciu typu path operation, pomocou ktorej získame zoznam všetkých meraní.

```python
@app.get("/api/measurements")
def list_of_measurements():
    with Session(get_db_engine()) as session:
        statement = select(Measurement)
        return session.exec(statement).all()
```



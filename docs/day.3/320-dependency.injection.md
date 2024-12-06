# Dependency Injection

## Introduction

"Dependency Injection" means, in programming, that there is a way for your code (in this case, your path operation
functions) to declare things that it requires to work and use: "dependencies".

And then, that system will take care of doing whatever is needed to provide your code with those needed
dependencies ("inject" the dependencies).

This is very useful when you need to:

* Have shared logic (the same code logic again and again).
* Share database connections.
* Enforce security, authentication, role requirements, etc.
* And many other things...
* All these, while minimizing code repetition.


## Dependency Injection and FastAPI

* `Depends`

## Funkcia `get_session()`

Vytvorime session dependency podla https://fastapi.tiangolo.com/tutorial/sql-databases/?h=get_session#create-the-tables

```python
def get_session() -> Session:
    engine = create_engine(get_settings().db_uri)
    with Session(engine) as session:
        yield session
```

pouzijeme ako parameter funkcie (path operation):

```python
@app.get("/api/measurements")
def list_of_measurements(session: Annotated[Session, Depends(get_session)]):
   pass
```


## Ďalšie zdroje

* [Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/?h=dependency+injection)
* [Session Dependency](https://fastapi.tiangolo.com/tutorial/sql-databases/?h=get_session#create-the-tables)
* Nette: [Dependency Injection](https://doc.nette.org/cs/dependency-injection)

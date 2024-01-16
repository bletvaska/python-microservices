# Dependency Injection

## Introduction


## Dependency Injection and FastAPI

* `Depends`

Urobíme modul `dependencies.py`.


## Funkcia `get_session()`

```python
def get_session() -> Session:
    engine = create_engine(get_settings().db_uri)
    with Session(engine) as session:
        yield session
```


## Funkcia `get_settings()`

```python
@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    print(f'Loading settings for: {settings.environment}.')
    return settings
```

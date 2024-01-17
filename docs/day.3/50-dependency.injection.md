# Dependency Injection

## Introduction


## Dependency Injection and FastAPI

* `Depends`

Urobíme modul `dependencies.py`.


## Funkcia `get_settings()`

```python
@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    print(f'Loading settings for: {settings.environment}.')
    return settings
```


## Získanie nastavení v kóde

Dve možnosti:

* priamym volaním

   ```python
   settings = get_settings()
   ```

* parameter funkcie:

   ```python
   @router.get("/api/measurements")
   def get_all_measurements(settings: Settings = Dependes(get_settings)):
      pass
   ```


## Funkcia `get_session()`

```python
def get_session() -> Session:
    engine = create_engine(get_settings().db_uri)
    with Session(engine) as session:
        yield session
```




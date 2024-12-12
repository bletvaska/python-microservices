# Project Structure Refactoring

## Architektúra projektu

Pre REST API urobime samostatny balik a v nom modul `measurements.py`, ktory bude obsahovat vsetky HTTP metody pre pracu so
subormi. Štruktúra projektu bude nasledne vyzerat takto:

```
project
├── weather
│   ├── routers
│   │   ├── measurements.py
│   │   └── __init__.py
│   ├── models
│   │   ├── measurement.py
│   │   ├── settings.py
│   │   └── __init__.py
│   ├── __init__.py
│   └── main.py
├── pyproject.toml
└── readme.md
```

Na to, ako sa da projekt upravit, sa da pozriet napr. do [tohto projektu](https://github.com/zhanymkanov/fastapi-best-practices?tab=readme-ov-file), ktory zhrna best practices pri tvorbe aplikacii s FastAPI.

## Modul `measurements.py`

```python
from fastapi import APIRouter

router = APIRouter()

@router.get('/api/measurements')
async def get_measurements(session: Annotated[Session, Depends(get_db_session)],
                           city: str = None,
                           start_date: date = None,
                           end_date: date = None):
    ...
```


## Modul `main.py`

```python
from .routers import measurements
# from .router.measurements import measurements_router

app = FastAPI()
app.include_router(measurements.router)
```

Metóda `.include_router()` má však aj parametre. Jednou z nich je aj `prefix`:

```python
app.include_router(
   measurements.router,
   prefix='/api/measurements'
)
```

Na základe prefixu je ale potrebné upraviť aj cesty pre funkcie _path operation_.


## Zdroje

* [Bigger Applications - Multiple Files](https://fastapi.tiangolo.com/tutorial/bigger-applications/#an-example-file-structure)

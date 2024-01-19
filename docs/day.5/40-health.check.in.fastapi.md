# Health Check a FastAPI



* pre FastAPI je na to modul https://github.com/Kludex/fastapi-health

najprv ho nainstalujeme

```bash
$ poetry add fastapi-health
```


vytvorime samostatny endpoint v subore `api/healthcheck.py`:

```python
from pathlib import Path
import http

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi_health import health

from weather.dependencies import get_session

router = APIRouter()


@router.get('/api/healthy')
def healthy(request: Request):
    return 'OK'


@router.get('/api/unhealthy')
def unhealthy():
    raise HTTPException(
        status_code=http.HTTPStatus.INTERNAL_SERVER_ERROR,
        detail="Something strange happened."
    )


def is_database_online(session: bool = Depends(get_session)):
    return session


def is_healthy():
    return not Path('unhealthy').exists()


router.add_api_route(
    "/healthz",
    health([is_database_online, is_healthy])
)
```

nakoniec len pridame smerovac do _FastAPI_ aplikacie v subore `main.py`:

```python
from weather.api.healthcheck import router as healthcheck_router

app.include_router(healthcheck_router)
```


## Testovanie

mozeme overit funkcionalitu z prikazoveho riadku:

```bash
$ http http://localhost:8000/healthz
```

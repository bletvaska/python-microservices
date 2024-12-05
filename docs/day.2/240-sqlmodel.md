# SQLModel

## Inštalácia

```bash
$ poetry add sqlmodel
```

## Aktualizácia modelu

Upravíme model `Measurement` tak, že:

* predkom modelu bude trieda `SQLModel`, a
* pridáme navyše jednu členskú premennú `id`, ktorá bude reprezentovať primárny kľúč

```python
from datetime import datetime
from sqlmodel import SQLModel, Field

class Measurement(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    temperature: float  # metric °C
    humidity: int  # %
    pressure: int  # hPa
    sunrise: datetime
    sunset: datetime
    country: str
    city: str
    dt: datetime
```


## Rozšírenie konfigurácie o DB URL

```python
class Settings(BaseSettings):
    api_token: str | None = None
    interval: int = 60
    db_uri: str = 'sqlite:///weather.sqlite'
```


## Vytvorenie schémy

```python
app = FastAPI(lifespan=lifespan)

# create db schema
engine = create_engine(get_settings().db_url)
SQLModel.metadata.create_all(engine)
```

To, či je schéma vytvorená, môžeme overiť tým, že:

* vznikne súbor s databázou, a
* v databáze sa bude nachádzať tabuľka `Measurement`

To overíme pomocou SQLite klienta `litecli`.

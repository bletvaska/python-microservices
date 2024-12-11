# Logovanie

* co je to logovanie?
* urovne logovacich sprav
* nasa mikrosluzba sa bude spustat v kontajneri
  * odporucanie je logovat na standardny vystup
* python ma podporu pre logovanie v standardnej kniznici
  * je komplexna
  * zvlada aj rotovanie log suboro
  * je potrebne poznat aj dalsie veci, ako handler, logger, formatter
* kedze aplikaciu budeme spustat v kontajneroch, plati obecne pravidlo: loguje sa na standardny vystup
* my pouzijeme nieco jednoduchsie - modul loguru


## Instalacia

```bash
$ poetry add loguru
```

## pouzitie

```python
from loguru import logger

logger.info('New connection')
```


## Logovanie FastAPI a Uvicorn/Starlette

* problem: kazdy loguje inde a inac (iny styl logovacich sprav)
* zjednotime logovanie tymto kodom, ktory umiestnime do suboru `logging.py`

```python
# stolen from:
# https://medium.com/@muh.bazm/how-i-unified-logging-in-fastapi-with-uvicorn-and-loguru-6813058c48fc
import logging

from loguru import logger


class InterceptHandler(logging.Handler):
    def emit(self, record):
        # Get corresponding Loguru level
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller to get correct stack depth
        frame, depth = logging.currentframe(), 2
        while frame.f_back and frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )


def init_logging():
    # Remove existing handlers
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    # Intercept standard logging
    logging.basicConfig(handlers=[InterceptHandler()], level=logging.DEBUG)

    loggers = (
        "uvicorn",
        "uvicorn.access",
        "uvicorn.error",
        "fastapi",
        "asyncio",
        "starlette",
    )

    for logger_name in loggers:
        logging_logger = logging.getLogger(logger_name)
        logging_logger.handlers = []
        logging_logger.propagate = True
```

logovanie inicializujeme pomocou vytvorenej funkcie `init_logging()` v module `main.py` vo funkcii `lifespan()`. funkciu zavolame hned na zaciatku:

```python
@asynccontextmanager
async def lifespan(app: FastAPI):
    # setup
    init_logging()
    ...
```

nasledne vsade, kde pouzivame funkciu `print()` mozeme pouzit logovanie pomocou `loguru`:

```python
from loguru import logger

logger.debug('hello world')
```

##


## Konfigurácia úrovne logovania Loguru

premenná prostredia `LOGURU_LEVEL`. môžeme teda rozšíriť aj konfiguračný súbor s premennými prostredia `.env`:

```dotenv
LOGURU_LEVEL=INFO
```

ak to spustíme, tak sa to zrúbe. to preto, že Pydantic Settings nepripúšťa iné premenné prostredia v súbore `.env`
okrem tých, ktoré tam máme. aby ich povolil, treba pridať extra nastavenie:

```python
class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        extra='allow',
    )
```

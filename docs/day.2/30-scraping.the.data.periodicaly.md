# Opakovane stahovanie dat

## Lifespan

mechanizmus, kedy vieme vykonať kód

* **predtým**, ako sa aplikácia spustí a začne prijímať a obsluhovať požiadavky od klientov, a
* **potom**, ako skončí s prijímaním požiadaviek a začne sa vypínať

## Kód

Najpr vytvoríme funkciu `lifespan()`, ktorá bude **generátorom**. Táto funkcia bude používať dekorátor
`@asynccontextmanager`.

```python
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
   # setup
   logger.info('Weather App is starting.')

   yield

   # teardown
   logger.info('Weather App is shutting down.')
```

Následne pri vytváraní inštancie `FastAPI` mu túto funkciu odovzdáme ako parameter `lifespan`. To znamená, že
funkcia musí existovať pred vytvorením objektu aplikácie:

```python
from fastapi import FastAPI

app = FastAPI(lifespan=lifespan)
```

## Advanced Python Scheduler

Na periodicky sa opakujúce úlohy použijeme
balík [Advanced Python Scheduler](https://apscheduler.readthedocs.io/en/master/?badge=latest)

Python library that lets you schedule your Python code to be executed later, either just once or periodically. You
can add new jobs or remove old ones on the fly as you please. If you store your jobs in a database, they will also
survive scheduler restarts and maintain their state. When the scheduler is restarted, it will then run all the jobs
it should have run while it was offline

### Inštalácia

```bash
$ poetry add apscheduler
```

### Použitie

Najprv vytvoríme funkciu (Job), ktorej spúšťanie naplánujeme. Bude vyzerať takto:

```python
def retrieve_weather_data():
   pass
```

Následne naplánujeme jej spúšťanie počas inicializácie aplikácie vo funkcii `lifespan`. Celý časovač vypneme pri
skončení aplikácie. Upravená fukcia `lifespan` bude teda vyzerať takto:

```python
from contextlib import asynccontextmanager
from apscheduler.schedulers.background import BackgroundScheduler


@asynccontextmanager
async def lifespan(app: FastAPI):
   # setup
   logger.info('Weather App is starting.')

   # start scheduler
   scheduler = BackgroundScheduler()
   scheduler.add_job(retrieve_weather_data, "interval", minutes=1)
   scheduler.start()

   yield

   # teardown
   logger.info('Weather App is shutting down.')
   scheduler.shutdown()
```

<!--
najprv nainstalujeme balik `fastapi-restful`, ktory ma zavislost na baliku `typing-inspect`:

```python
$ poetry add fastapi-restful typing-inspect
```

a vytvorime funkciu, ktora sa bude spustat kazdych 10 sekund:

```python
@app.on_event("startup")
@repeat_every(seconds=10)
def retrieve_weather_data():
    print('>> retrieving')
```


## Opakovane stahovanie dat

Refaktorujeme nas kod tak, aby sme data stiahli kazdych 20 minut a ulozili sme ich do suboru `weather.json`:

```python
@app.on_event("startup")
@repeat_every(seconds=20 * 60)
def retrieve_weather_data():
    print('>> retrieving')

    params = {
        'q': 'kosice',
        'units': 'metric',
        'appid': '9e547051a2a00f2bf3e17a160063002d',
        'lang': 'eng'
    }
    response = httpx.get('https://api.openweathermap.org/data/2.5/weatherx', params=params)

    if response.status_code == http.HTTPStatus.OK:
        with open('weather.json', 'w') as file:
            json.dump(response.json(), file, indent=2)
    else:
        print('>> ta status kod je iny ako 200. ta zrob daco.')
```


## Aktualizacia API

Nase REST API upravime zasa tak, ze ked pouzivatel poziada o data, posunieme mu tie, ktore mame ulozene:

```python
@app.get('/weather')
def get_weather():
    print('>> get weather')

    with open('weather.json') as file:
        return json.load(file)
```
-->

# Opakovane stahovanie dat

## Lifespan

mechanizmus, kedy vieme vykonať kód

* **predtým**, ako sa aplikácia spustí a začne prijímať a obsluhovať požiadavky od klientov, a
* **potom**, ako skončí s prijímaním požiadaviek a začne sa vypínať

**Upozornenie:** Jedná sa o náhradu dekorátora `@app.on_event()`, ktorý je označený ako [`deprecated`](https://fastapi.tiangolo.com/reference/apirouter/?h=on_event#fastapi.APIRouter.on_event).


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

Najprv vytvoríme funkciu, ktorej spúšťanie naplánujeme. Na začiatok bude vyzerať takto:

```python
def retrieve_weather_data():
   print('>> Retrieving data')
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
   scheduler.add_job(retrieve_weather_data, "interval", seconds=10)
   scheduler.start()

   yield

   # teardown
   logger.info('Weather App is shutting down.')
   scheduler.shutdown()
```


## Lab: Funkcia `retrieve_weather_data()`

Vytvorte funkciu `retrieve_weather_data()`, ktorá stiahne dáta o počasí pre Košice a zo získaných dát vytvorí objekt
typu `Measurement`.


```python
def scrape_data():
    print('>> scraping data')

    # scrape data
    settings = get_settings()
    url = 'https://api.openweathermap.org/data/2.5/weather'

     params = {
         'q': 'kosice',
         'units': 'metric',
         'appid': settings.api_token
     }
     response = httpx.get(url, params=params)
     data = response.json()

     # create measurement
     measurement = Measurement(
         dt=data['dt'],
         city=data['name'],
         country=data['sys']['country'],
         temperature=data['main']['temp'],
         humidity=data['main']['humidity'],
         pressure=data['main']['pressure'],
         sunrise=data['sys']['sunrise'],
         sunset=data['sys']['sunset'],
     )
     print(measurement)
```

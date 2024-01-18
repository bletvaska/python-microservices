# Output Model

_Output mode_ sa používa na "prebalenie" odpovede pre klienta. Hlavným zámerom je:

* odstrániť z odpovede niektoré (hlavne citlivé) kľúče, ako napr. heslá, jedinečné identifikátory v databáze a pod.
* pridať do odpovede niektoré kľúče, ako napr. URL adresa na detail daného objektu alebo údaje, ktoré vzniknú
  kompozíciou s ďalšími údajmi (napr. album (jeden model) a jeho skladby (druhý model))


## Vytvorenie modelu pre odpoved

Výstupný model môže vyzerať nasledovne:

```python
class MeasurementOut(BaseModel):
    dt: datetime  # UTC
    temperature: float  # °C
    humidity: float
    pressure: float  # hPa
    city: str
    country: str
    wind_speed: float  # m/s
    wind_direction: int  # °
    sunrise: datetime  # UTC
    sunset: datetime  # UTC
    icon: str
```


## Aplikovanie modelu

```python
@router.get('/api/measurements/{slug}', response_model=Measurement)
def get_last_measurement(slug: int, session: Session = Depends(get_session)):
   statement = select(Measurement).where(Measurement.id == slug)
   measurement = session.exec(statement).one_or_none()

   if measurement is None:
      return {
         "error": f"Measurement {slug} not found."
      }

   return measurement
```

Otestujeme:

```bash
$ http http://localhost:8000/api/measurements/1
```


## Pridanie linky na zdroj

Odporucanie - kazdy zdroj, ktory vratite, by mal obsahovat aj URL adresu, kde sa viete dostat k jeho detalu.

Rozsirime teda model o clensku premennu `url` (alebo `link`):

```python
class MeasurementOut(BaseModel):
    url: HttpUrl = None
```

Ak tam chceme dostat data, spravime v modeli validator:

```python
 @validator('url', always=True)
 def set_file_url(cls, value, values):
     return f'http://localhost:8000/{values["id"]}'
```


## Refaktoring

URL adresa sa bude menit medzi nasadeniami, takze ju dame do konfiguracie:

```python
class Settings(BaseSettings):
    environment: str = 'production'
    db_uri: str = 'sqlite:///database.sqlite'
    api_token: str | None = None
    base_url: HttpUrl = 'http://localhost:8000'

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        env_prefix='weather_'
    )
```

A pouzijeme ju vo validatore:

```python
 @validator('url', always=True)
 def set_file_url(cls, value, values):
     return f'{get_settings().base_url}/{values["id"]}'
```


## Links

* [FastAPI: Response Model - Return Type](https://fastapi.tiangolo.com/tutorial/response-model/)

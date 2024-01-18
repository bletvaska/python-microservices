# Output Model

_Output mode_ sa používa na "prebalenie" odpovede pre klienta. Hlavným zámerom je:

* odstrániť z odpovede niektoré (hlavne citlivé) kľúče, ako napr. heslá, jedinečné identifikátory v databáze a pod.
* pridať do odpovede niektoré kľúče, ako napr. URL adresa na detail daného objektu alebo údaje, ktoré vzniknú
  kompozíciou s ďalšími údajmi (napr. album (jeden model) a jeho skladby (druhý model))

Výstupný model môže vyzerať nasledovne:

```python
class Measurement(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
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

## Links

* [FastAPI: Response Model - Return Type](https://fastapi.tiangolo.com/tutorial/response-model/)
*

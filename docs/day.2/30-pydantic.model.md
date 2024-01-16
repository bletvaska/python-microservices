# Pydantic Model

![Pydantic Logo](https://pydantic.dev/imgs/social.png)

[Pydantic](https://docs.pydantic.dev/latest/) is the most widely used data validation library for Python.

Balík `pydantic` najprv nainštalujeme:

```bash
$ poetry add pydantic
```
a pre lepsiu pracu si nainstalujeme aj plugin pre pycharm, aby isiel `pydantic`. otvorime nastavenia cez `File >
Settings > Plugins` a nechame vyhladat a nainstalovat plugin s nazvom `Pydantic`.


## Výsledný model

Modely budeme ukladať v module `models.py`.

Model pre reprezentáciu merania môže vyzerať takto:

```python
from datetime import datetime

from pydantic import BaseModel


class Measurement(BaseModel):
    dt: datetime            # UTC
    temperature: float      # °C
    humidity: float
    pressure: float         # hPa
    city: str
    country: str
    wind_speed: float       # m/s
    wind_direction: int     # °
    sunrise: datetime       # UTC
    sunset: datetime        # UTC
    icon: str
```


## Otestovanie vytvoreného modelu

Na základe vytvoreného modelu môžeme vytvoriť meranie aj ručne pomocou nastroja `ipython`:

```python
from weather.models import Measurement

measurement = Measurement(
   dt=0,
   temperature=1.2,
   humidity=90,
   pressure=1021,
   city="Kosice",
   country='sk',
   wind_speed=0,
   wind_direction=0,
   icon='01d',
   sunrise=0,
   sunset=0
)
```

Pristupovať k jednotlivým položkám merania môžeme následne pomocou operátora `.` nasledovne:

```python
>>> measurement.city
'Kosice'
>>> measurement.pressure
1021
```

# Zoznam miest

Aktuálne vieme sťahovať merania iba pre jedno mesto a aj to len pre Košice. Upravíme teda konfiguráciu tak, že do nej vložíme zoznam miest, pre ktoré budeme v pravidelných intervaloch sťahovanie informácie o počasí.


## Aktualizácia konfigurácie

```python
class Settings(BaseSettings):
    api_token: str | None = None
    interval: int = 60
    db_uri: str = 'sqlite:///weather.sqlite'
    cities: list[str] = []
```


## Premenné prostredia

Keď budeme zoznam písať do premenných prostredia (do súboru `.env`), musí byť tento zoznam napísaný ako JSON zoznam:

```dotenv
WEATHER_CITIES=["kosice","presov","poprad"]
```

## Lab: Aktualizácia funkcie `scrape_weather_data()`

Aktualizujte funkciu `scrape_weather_data()` tak, aby stiahol a uložil informácie o aktuálnom počasí pre všetky mestá zo zoznamu miest v konfigurácii.

```python
def scrape_data():
    print('>> scraping data')

    # scrape data
    settings = get_settings()
    url = 'https://api.openweathermap.org/data/2.5/weather'

    for city in settings.cities:
        params = {
            'q': city,
            'units': 'metric',
            'appid': settings.api_token
        }
        # the rest of code
```

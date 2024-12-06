# Nastavenia

aktualne porušujeme odporúčania metodólogie [Twelve-Factor App](https://12factor.net), pretože v kóde máme napevno
napísaný token pre prístup k API služby openweathermap.org. Miesto toho, aby bol jeho súčasťou (aj Github sa bude
sťažovať) ho uložíme do súboru s nastaveniami, ktoré sa načítajú pomocou premenných prostredia.

Na to použijeme modul `pydantic-settings`, ktorý je rozšírením modulu `pydantic` práve o možnosť používať modely pre
nastavenia aplikácie.

## Inštalácia

Tento modul bude súčasťou štandardných závislostí projektu, tkaže ho pridáme takto:

```bash
$ poetry add pydantic-settings
```

## Modely

Všetky modely, ktoré vytvoríme pre náš projekt, umiestnime do balíka `models`. Najprv ho teda vytvoríme.

## Model `Settings`

Zatiaľ bude jedinou vecou, ktorú budeme vedieť nastaviť, práve API token pre službu openweathermap.org. Model pre
nastavenia sa bude volať `Settings`, uložíme ho do modulu `settings.py` do balíka `models`  a bude vyzerať nasledovne:

```python
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
   api_token: str | None = None

   model_config = SettingsConfigDict(
      env_file_encoding='utf-8',
      env_file='.env',
      env_prefix='WEATHER_',
   )
```

## Použitie nastavení

Nastavenia použijeme priamo vo funkcii `get_weather()` takto:

```python
@app.get('/api/weather', description='get weather info for given city')
async def get_weather(city: str, units: str = 'metric'):
   settings = Settings()
   url = 'https://api.openweathermap.org/data/2.5/weather'
   params = {
      'q': city,
      'units': units,
      'appid': settings.api_token
   }
   response = httpx.get(url, params=params)
   return response.json()
```

Premenné prostredia:

* cez PyCharm
* cez súbor `.env` - preferovaný spôsob
   * `.gitignore`

## Nastavenia a cache

Ku načítaniu nastavení dôjde zakaždým, keď príde požiadavka na cestu `/api/weather`. Premenné prostredia sa však
nastavujú pred spustením aplikácie a počas jej behu sú nemenné. Stačí nám teda, ak ich načítame len raz.

To môžeme síce spraviť pomocou globálnej premennej na úrovni modulu, ale modulov, kde bude treba mať nastavenia,
bude samozrejme viac.

Miesto toho využijeme dekorátor z balíka `functools` s názvom `cache` alebo `lru_cache`, ktoré zabezpečia, že
volanie funkcie bude cachované. Vytvoríme si teda samostatnú funkciu `get_settings()` v osobitnom module
`dependencies.py` (pretože závislostí bude tiež viac), ktorá vráti načítané nastavenia aplikácie.

```python
@cache
def get_settings():
   return Settings()
```

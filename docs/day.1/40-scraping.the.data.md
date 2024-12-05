# Stiahnutie aktuálneho počasia

## HTTP klient

k dispozícii máme niekoľko knižníc, ktoré môžeme použiť, napr:

* [requests](https://requests.readthedocs.io/en/latest/) - Requests is a simple, yet elegant, HTTP library.
* [httpx](https://www.python-httpx.org) - HTTPX is a fully featured HTTP client library for Python 3.

Modul `httpx` používa rovnaké API ako má modul `requests`, ale pridáva podporu pre asynchrónne použitie. Pre našu
aplikáciu teda použijeme modul `httpx`.

## Prvé kroky s `httpx`

Základy si vyskúšame v IPython-e:

```python
import httpx

url = 'https://api.openweathermap.org/data/2.5/weather'
params = {
   'q': 'kosice,sk',
   'appid': '9e547051a2a00f2bf3e17a160063002d'
}
response = httpx.get(url, params=params)
response.json()
```

## Vytvorenie path operation

Na základe experimentov pomocou IPython-u vytvoríme funkciu `get_weather()`, ktorá bude reprezentovať _path
operation_ na ceste `/api/weather`:

```python
@app.get('/api/weather')
async def get_weather():
   url = 'https://api.openweathermap.org/data/2.5/weather'
   params = {
      'q': 'kosice,sk',
      'appid': '9e547051a2a00f2bf3e17a160063002d'
   }
   response = httpx.get(url, params=params)
   return response.json()
```

Otestovať ju môžeme z príkazového riadku pomocou HTTP klienta `httpie`:

```bash
$ http http://localhost:8000/api/weather \
  q==kosice \
  appid=9e547051a2a00f2bf3e17a160063002d
```

## Prípustné vstupné parametre

```python
async def get_weather(city: str, units: Literal['metric', 'standard', 'imperial'] = 'metric'):
```

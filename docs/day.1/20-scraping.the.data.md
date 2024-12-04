# Stiahnutie aktuálneho počasia

## HTTP klient

použijeme modul `httpx`

príklad použitia:

```python
url = 'https://api.openweathermap.org/data/2.5/weather'
params = {
   'q': 'kosice,sk',
   'appid': '9e547051a2a00f2bf3e17a160063002d'
}
response = httpx.get(url, params=params)
return response.json()
```

## Vytvorenie path operation

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


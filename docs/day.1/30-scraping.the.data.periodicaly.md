# Opakovane stahovanie dat


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

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

Refaktorujeme nas kod tak, aby sme data stiahli kazdych 20  minut a ulozili sme ich do suboru `weather.json`:

```python
@app.on_event("startup")
@repeat_every(seconds=10)
def retrieve_weather_data():
    print('>> retrieving')
```


## Aktualizacia API

Nase REST API upravime zasa tak, ze ked pouzivatel poziada o data, posunieme mu tie, ktore mame ulozene:

```python
@app.get('/weather')
def get_weather(q: str, units: str = 'metric', lang: str = 'en'):

```

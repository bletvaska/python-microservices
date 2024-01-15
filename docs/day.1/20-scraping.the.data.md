# Stiahnutie aktuálneho počasia

## Instalacia ipython
```python
$ poetry add  --group dev ipython httpie
```

## Pouzitie modulu httpx

```python
import httpx

response = httpx.get("https://api.openweathermap.org/data/2.5/weather&unitx=metric&q=kosice,sk&appid=")
```


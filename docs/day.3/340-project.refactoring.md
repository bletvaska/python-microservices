# Project Structure Refactoring

## Architektúra projektu

Pre REST API urobime samostatny balik a v nom modul files.py, ktory bude obsahovat vsetky HTTP metody pre pracu so
subormi. Štruktúra projektu bude nasledne vyzerat takto:

```
project
├── weather
│   ├── routers
│   │   ├── measurements.py
│   │   └── __init__.py
│   ├── models
│   │   ├── measurement.py
│   │   ├── settings.py
│   │   └── __init__.py
│   ├── __init__.py
│   └── app.py
├── pyproject.toml
└── readme.md
```


## Modul `measurements.py`


## Zdroje

* [Bigger Applications - Multiple Files](https://fastapi.tiangolo.com/tutorial/bigger-applications/#an-example-file-structure)

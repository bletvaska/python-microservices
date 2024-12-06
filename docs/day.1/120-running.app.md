# Spustenie aplikacie

## Running the App from CLI

nasledne mozeme aplikaciu spustit prikazom z korenoveho priecinku projektu

```bash
$ uvicorn pokedex.main:app --reload
```

alebo ako modul:

```bash
$ python -m pokedex.main
```

## Running with PyCharm

1. `Run > Edit Configurations...`
2. `+ > Python`
3. vyplnit:
   * Name: Run Microservice
   * module: `weather.main`
   * parameters: --reload
   * modify options: Emulate terminal in output console

## Running with Visual Studio Code

mozem pridat spustac priamo pre FastAPI, ktoremu VS Code rozumie. vysledok bude vyzerat takto:

```json
{
   "version": "0.2.0",
   "configurations": [
      {
         "name": "Python: FastAPI",
         "type": "python",
         "request": "launch",
         "module": "uvicorn",
         "args": [
            "pokedex.main:app"
         ],
         "jinja": true,
         "justMyCode": true
      }
   ]
}
```

alebo univerzalne mozeme vytvorit spustac pre Python modul:

```json
{
   "version": "0.2.0",
   "configurations": [
      {
         "name": "Python: Module",
         "type": "python",
         "request": "launch",
         "module": "pokedex.main",
         "justMyCode": true
      }
   ]
}
```

## Refactoring with module `__main__.py`

V balíku vytvoríme samostatný modul `__main__.py`, ktorý sa spustí ako prvý, keď aplikáciu budeme spúšťať ako balík.
Tento súbor nahradí význam volania

```python
if __name__ == '__main__':
```

v súbore `main.py`, ktorý tým pádom môžeme z tohto súboru vypustiť. Obsah súboru `__main__.py` bude nasledovný:

```python
import uvicorn

uvicorn.run('weather.main:app', reload=True,
            host='0.0.0.0', port=8000)
```

Spúšťať aplikáciu tým pádom už môžeme na úrovni balíka bez uvedenia modulu:

```bash
$ python -m weather
```

zdroje:

* [__main__.py in Python Packages  ](https://docs.python.org/3/library/__main__.html#main-py-in-python-packages)

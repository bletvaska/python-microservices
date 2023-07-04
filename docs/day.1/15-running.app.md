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

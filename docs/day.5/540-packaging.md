# Zabalenie aplikacie


```bash
$ poetry build
```

**Poznamka:** Moze sa zrubat kvoli suboru `readme.md`, pretoze potrebuje subor `README.md`. Staci ho len premenovat.

vytvori priecinok `dist` a v nom:

* balik `.tgz`
* instalacny balik `.whl`


nainstalovat balik potom mozeme z prikazoveho riadku spolu s jeho zavislostami prikazom:

```bash
$ pip install ./weather.whl
```

## Start Script

```toml
[tool.poetry.scripts]
start_app = 'weather.main:main'
```

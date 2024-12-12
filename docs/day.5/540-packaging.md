# Zabalenie aplikacie


```bash
$ poetry build
```

vytvori priecinok `dist` a v nom:

* balik `.tgz`
* instalacny balik `.whl`


nainstalovat balik potom mozeme z prikazoveho riadku spolu s jeho zavislostami prikazom:

```bash
$ pip install ./weather.whl
```

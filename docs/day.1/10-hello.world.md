# FastAPI

rámec FastAPI, vlastnosti, inštalácia, prvé použitie

* [porovnanie s inými rámcami a technológiami](https://www.techempower.com/benchmarks/#section=data-r20&hw=ph&test=query&l=v2p4an-db&a=2)


## Inštalácia

Ramec FastAPI nainstalujeme pomocou nastroja `poetry`. Okrem neho vsak budeme potrebovat aj ASGI server `uvicorn`. Oba baliky nainstalujeme prikazom:

```bash
$ poetry add fastapi uvicorn[standard]
```


## Hello World!

aby sme sa zbytocne nezdrziavali, pouzijeme rovno kostru aplikacie so vsetkym potrebnym. do svojho modulu `main.py` 
vlozte tento kod:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
    return "Hello, World!"


def main():
    uvicorn.run('fishare.main:app', reload=True,
                host='127.0.0.1', port=8000)

if __name__ == '__main__':
    main()
```

Funkciu `hello()` budeme nazývať _path operation_.


## Nastavenie spravneho interpretera

Ak IDE nerozpoznava pouzite balicky (napr. podciarkuje priamo v importe balik `fastapi`), je potrebne zvolit spravny interpreter jazyka Python. Konkretne ten, ktory je pozity v prostredi vytvorenom pomocou nastroja `poetry`.


### Zistenie cesty interpretera jazyka Python

zobrazime si zoznam virtualnych prostredi, ktore pre nas projekt existuju:

```bash
$ poetry env list
```

informacie o aktualnom prostredi spolu s cestou veducou k interpreteru, ziskate prikazom

```bash
$ poetry env info
```

v pripade, ze sa nezobrazi ziadne virtualne prostredie, je potrebne ho vytvorit. to je mozne napriklad spustenim shell-u:

```bash
$ poetry shell
```

nasledne je potrebne nainstalovat vsetky balicky prikazom:

```bash
$ poetry install
```


### Visual Studio Code

v pravom dolnom rohu treba kliknut na oznacenie interpreteru jazyka Python a nasledne zvolit cestu veducu k prostrediu, ktore bolo vytvorene pomocou nastroja `poetry`. ak nie je uvedena v zozname, tak treba zvolit polozku na pridanie cesty `+ Enter interpreter path...`.

rovnaku ponuku vieme zobrazit cez `Command Palette...` a zadanim polozky `Python: Select Interpreter`.

ak sme vybrali interpreter spravne, nezname balicky prestanu byt podciarknute a rovnako tak zacne fungovat aj automaticke doplnovanie kodu.


### PyCharm

<!--
#### Python Project Interpreter Update

Aktualne sa bude PyCharm stazovat na to, ze nepozna jednotlive moduly, ktore pouzivame a vela veci v nasom kode bude podciarknutych cervenou farbou. to je preto, ze o virtualne prostredie sa momentalne stara `poetry` a _PyCharm_ o tom nevie. aktualizujeme teda nastavenia interpretra:

1. otvorime `File` > `Settings`
2. v dialogovom okne nasledne `Project: fishare` > `Python Interpreter`
3. pri polozke interpretera klikneme na zubate koliesko a klikneme na polozku `Add...`
4. zo zoznamu vlavo najprv vyberieme `Poetry Environment` a zo zoznamu `Existing environment` vyberieme interpreter nasho projektu


#### Nastavenie spustania projektu v Pycharm-e

mame v podstate dva sposoby:

1. staci pravym tlacidlom mysi kliknut na modul `main.py` a spustit ho. tym sa vytvori spustac sam. toto je pouzitelne v pripade jednomodulovych projektov. nas bude komplexnejsi, takze toto robit nebudeme.

2. vytvorit samostatnu konfiguraciu pre spustenie projektu cez polozku `Edit Configuration`:

    * module name - `fishare.main`
    * interpereter - poetry set
    * nastavit workdir na korenovy priecinok projektu
-->

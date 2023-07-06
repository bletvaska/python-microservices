# Python 202 (Microservices with Python)

rozsah: 4-5 dní

Počas tohto kurzu účastníci vytvoria jednoduchú mikroslužbu na ukladanie súborov po vzore služby file.io.
Mikroslužba bude vytvorená v modernom a populárnom mikro webovom rámci [FastAPI](https://fastapi.tiangolo.com),
validovať údaje budeme pomocou populárneho modulu [Pydantic](https://pydantic.dev) a perzistenciu zabezpečíme
pomocou ORM modulu [SQLModel](https://sqlmodel.tiangolo.com), ktorý je postavený na populárnom ORM
module [SQLAlchemy](https://www.sqlalchemy.org). Okrem REST API vytvoríme aj webové používateľské
rozhranie pomocou šablónovacieho systému [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/). Na záver aplikáciu
zabalíme do Docker obrazu a pripravíme ju na použitie v klastri.

Znalosť jazyka Python na tomto školení je nutná.


## Preberané témy

* správa projektu pomocou [Poetry](https://python-poetry.org)
* dizajn vytváraného REST API
* rámec [FastAPI](https://fastapi.tiangolo.com) na tvorbu REST API
* modul [Pydantic](https://pydantic.dev) na tvorbu modelov
* ORM modul [SQLModel](https://sqlmodel.tiangolo.com) pre zabezpečenie perzistencie údajov do databázy
* stránkovanie výsledkov
* práca s dátumom a časom
* modul Faker pre vytváranie testovacích údajov
* modul `pathlib`
* ošetrovanie chýb
* spracovanie konfigurácie pomocou `.env` súborov
* šablónovací systém [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/)
* kontrola stavu mikroslužby (healthcheck)
* zbieranie metrík
* balenie Python aplikácií do Docker obrazov
* vytvorenie balíka

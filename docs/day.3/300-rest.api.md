# REST API

čo je to REST API, paralela s jazykom SQL

Čo je to REST API?

REST API je založené na zdrojoch. v našom prípade bude zdrojom meranie (measurement). Platí niekoľko pravidiel:

* na tvorbu endpoint-ov sa používajú podstatné mená v množnom čísle
* to, čo sa má urobiť (sloveso), dodáva metóda HTTP protokolu
* údaje sa prenášajú pomocou formátu JSON

Tým sa zabezpečí vytvorenie API, ktoré nebude tesne naviazané na konkrétnu funkcionalitu (napr.
`/api/get_all_measurements`). Takýto prístup by spôsobil:

* vytvorenie obrovského množstva endpoint-ov, čím by bolo API veľmi neprehľadné
* na každý typ požiadavky by existoval samostatný endpoint

Typy vrátených hodnôt:

* jeden prvok - detail
* zoznam prvkov - list

## Návrh REST API

My spravíme REST API pre prístup k údajom o meraniach - pre zdroj `measurements`. Na to budeme používať len HTTP metódu
  `GET`.

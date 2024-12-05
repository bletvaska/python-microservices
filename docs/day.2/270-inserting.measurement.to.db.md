# Vloženie merania do databázy

Aktualizujeme funkciu `retrieve_weather_data()` o vloženie merania do databázy:

```python
# store measurement to db
with Session(get_db_engine()) as session:
    session.add(measurement)  # INSERT
    session.commit()
```


## Problém s konverziou času

Informácie o čase v info o počasí sú reprezentované v počte sekúnd od počiatku epochy. Model však očakáva, že to bude objekt typu `DateTime`. Pri vytváraní inštancie z modelu teda musíme:

* predtým, ako inštanciu vytvoríme, tak urobíme konverziu z celého čísla (počet sekúnd) na objekt typu `DateTime`, alebo
* vytvoríme validátor v Pydantic-u, aby to urobil za nás


## Konverzia pri vytváraní inštancie

Môžeme to urobiť pomocou funkcie `fromdatetime()`, ktorá sa nachádza v module `datetime` balíka `datetime`:

```python
from datetime import datetime

measurement = Measurement(
   dt=datetime.fromdatetime(data['dt']),
)
```

Rovnako to môžeme urobiť pomocou modulu `Pendulum`, ktorý ponúka silné možnosti pre prácu s časom a dátumom.

Najprv ho nainštalujeme:

```bash
$ poetry add pendulum
```

A použijeme:

```python
import pendulum

measurement = Measurement(
   dt=pendulum.from_timestamp(data['dt']),
)
```


## Vytvorenie Pydantic validátora

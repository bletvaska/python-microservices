# Jinja2 Templates

## Co je to sablonovaci system?

príklad mechanizmu pomocou f-reťazcov


## Jinja2

Jinja2 je veľmi populárny. Síce vychádza zo šablónovacieho systému, ktorý používa webový rámec Django, ale ten sa nedá použiť samostatne. Naopak - šablónovací systém Jinja2 používa mnoho ďalších nástrojov/knižníc:

* webové rámce - dá sa integrovať zrejme do väčšiny z nich, ako napr. do rámcov Flask, FastAPI, ...
* Ansible
* Salt


## Inštalácia

Balík so šablónovacím systémom Jinja2 je už nainštalovaný, pretože ho používa samotný Apache Airflow. Ak by ste ho však chceli používať pre svoje vlastné projekty, nainštalujete ho nasledovným príkazom:

```bash
# ak pouzivame poetry
$ poetry add jinja2

# ak pouzivame len pip
$ pip install jinja2
```


## Základy použitia

Začneme tým, že importujeme modul jinja2:

```python
>>> import jinja2
```

Hlavným komponent modulu je trieda Environment. Obsahuje rozličné zdieľané premenné, ako konfiguráciu, filtre a iné. Budeme ju používať na tvorbu šablón.

Začneme tým, že vytvoríme inštanciu triedy `Environment` bez parametrov:

```python
>>> env = jinja2.Environment()
```

Šablóna je vlastne reťazec, ktorý je veľmi podobný f-reťazcu. Rozdielom je, že miesto uzatvorenia premennej do jedných zložených zátvoriek túto premennú uzatvoríme do dvojitých. Jednoduchú šablónu vytvoríme takto:

```python
>>> template = env.from_string('Hello, {{ name }}!')
```

Nakoniec necháme šablónu vyrenderovať pomocou metódy `.render()`:

```python
>>> template.render()
'Hello, !'
```

Šablóna však bola vyrenderovaná bez dát. Ak chceme do šablóny na miesto {{ name }} dosadiť hodnotu, urobíme to pomocou parametrov metódy .render() takto:

```python
>>> template.render(name='World')
'Hello, World!'
```



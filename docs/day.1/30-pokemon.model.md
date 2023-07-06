# Pokemon Model


## Čo je to model?


## Databáza s Pokémonmi

Databáza s Pokémonmi sa nachádza v súbore `resources/pokedex.sqlite`. Na základe uložených dát vytvoríme model 
Pokémona, s ktorým budeme pracovať. 

Najprv sa teda pozrieme do samotných dát pomocou konzolového klienta [litecli](https://litecli.com). 


## LiteCLI

instalacia:

```bash
$ poetry add --group dev litecli
```

spustenie:

```bash
$ litecli weather.sqlite
```


## Analýza dát

Pozrime sa na štandardnú kartu Pokémena. Konkrétne na kartu s Pokémonom Pikachu:

![pikachu](../images/pikachu.jpg)

O každom Pokémonovi nás môžu zaujímať nasledujúce vlastnosti:

* `pokedex_number` - poradové číslo Pokémona v Pokédexe
* `name` - meno Pokémona
* `height` - výška Pokémona
* `weight` - hmotnosť Pokémona
* `classification` - 
* `type1` - 
* `type2` - 

A z týchto vlastností vytvoríme model.

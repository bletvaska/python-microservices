# Databáza s meraniami

* SQLite - bude v subore
* budeme pouzivat konzoloveho klienta [litecli](https://litecli.com).


## LiteCLI

instalacia:

```bash
$ poetry add --group dev litecli
```

## Použitie

spustenie:

```bash
$ litecli db.sqlite
```

pozrieme sa na zoznam tabuliek:

```bash
.tables
```

pozrieme sa na schému tabuľky `Measurement`>

```bash
.schema measurement
```

porátame počet záznamov v tabuľke `Measurement`:

```sql
SELECT count(*) FROM measurement;
```

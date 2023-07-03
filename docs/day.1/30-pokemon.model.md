# Pokemon Detail Model

## LiteCLI

instalacia:

```bash
$ poetry add --group dev litecli
```

spustenie:

```bash
$ litecli pokedex.sqlite
```

## Analýza

![pikachu](../images/pikachu.jpg)

o subore budeme chciet uchovavat:

* `slug` -
* `created_at` - datum a cas vytvorenia (nahratia) suboru
* `updated_at` - datum a cas poslednej aktualizacie suboru alebo jeho vlastnosti


# Pydantic a SQLModel


## Výsledný model

model pre reprezentaciu suboru moze vyzerat takto:

```python
from datetime import datetime
from pydantic import BaseModel, HttpUrl


class File(BaseModel):
    # id: int
    slug: str | None = None
    filename: str
    url: HttpUrl | None = None
    expires: datetime | None = None
    downloads = 0
    max_downloads = 1
    size: int
    mime_type: str = 'application/octet-stream'
    created_at: datetime | None = None
    updated_at: datetime | None = None
```

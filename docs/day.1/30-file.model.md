# File Detail Model


## Analyza
podla vzoru sluzby [file.io](http://file.io) vytvorime model, ktory bude reprezentovat subor (zdroj nasej sluzby). na jeho reprezentaciu pouzijeme modul [Pydantic](https://pydantic-docs.helpmanual.io/).

o subore budeme chciet uchovavat:

* `slug` -
* `filename` - nazov suboru, ktory pouzivatel nahra, povinny
* `url` - URL adresa, z ktorej bude mozne subor stiahnut
* `expires` - datum, dokedy bude subor ulozeny v sluzbe
* `downloads` - pocet stiahnuti suboru
* `max_downloads` - maximalny pocet stiahnuti, po jeho dosiahnuti sa subor zmaze
* `size` - velkost suboru v bytoch
* `mime_type` - typ obsahu suboru, v hlavicke HTTP oznacovany ako `content-type`
* `created_at` - datum a cas vytvorenia (nahratia) suboru
* `updated_at` - datum a cas poslednej aktualizacie suboru alebo jeho vlastnosti


## Vysledny model

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

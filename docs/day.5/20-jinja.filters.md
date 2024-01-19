# Jinja2 Filters


najprv vytvorime funkciu v subore `j2_filters.py`:

```python
from datetime import datetime

import pendulum


def j2_strftime(value, format='%Y-%m-%d') -> str:
    if isinstance(value, datetime):
        return value.strftime(format)

    elif isinstance(value, int):
        return pendulum.from_timestamp(value).strftime(format)

    return pendulum.parse(value).strftime(format)
```


potom upravime dependencies:

```python
@lru_cache
def get_templates():
    templates = Jinja2Templates(
        directory=Path(__file__).parent / 'templates',
    )

    # add filters
    templates.env.filters['strftime'] = j2_strftime

    return templates
```

a od tohto momentu vieme pouzivat filter nasledovne:

```python
{{ now | strftime('%H:%M') }}
```

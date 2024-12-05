# Lab: Funkcia `get_db_engine()`

V module `dependencies.py` vytvorte funkciu `get_db_engine()`, ktorá vráti objekt databázového enginu. Funkciu dekorujte dekorátorom `@cache`.

## Riešenie

```python
@cache
def get_db_engine():
    print('>> Loading database engine')
    return create_engine(get_settings().db_uri)
```

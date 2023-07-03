# Validators

validatory poskytuju mechanizmus, pomocou ktoreho mozeme overovat spravnost udajov, s ktorymi v ramci webovej sluzby budeme pracovat.

okrem toho vsak vieme validatory pouzivat aj na inicializovanie hodnot po vytvoreni objektu.


## Overenie MIME typu suboru

```python
@validator('mime_type')
def mime_type_must_contain_slash(cls, v):
   if '/' not in v:
      raise ValueError('must contain "/"')
   else:
      return v.lower()
```


## Inicializovanie casu vytvorenia

```python
@validator('created_at', always=True)
def set_created_at_to_now(cls, v):
   return datetime.now()
```


## Vytvorenie casu expiracie suboru

```python
@validator('expires', always=True)
def set_expiration_for_one_day(cls, v):
   return datetime.now() + timedelta(days=1)
```


## Vygenerovanie slug-u

```python
@validator('slug', always=True)
def set_secret_slug(cls, v):
   return secrets.token_urlsafe(settings.slug_length)
```


## Nazov suboru nemoze byt prazdny

```python
@validator('filename')
def filename_cant_be_empty(cls, v):
   if v == '':
      raise ValueError("can't be empty")
```

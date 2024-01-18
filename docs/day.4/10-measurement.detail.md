# Measurement Detail

Vytvorte nový funkciu typu _path operation_ s koncovým bodom `/api/measurements/{slug}`, ktorý vráti meranie na
základe jeho čísla. V prípade, že dané meranie neexistuje, vráťte nasledujúci dokument:

```json
{
   "error": "Measurement XXX not found."
}
```

### Riešenie

```python
@router.get('/api/measurements/{slug}')
def get_last_measurement(slug: int, session: Session = Depends(get_session)):
   statement = select(Measurement).where(Measurement.id == slug)
   measurement = session.exec(statement).one_or_none()

   if measurement is None:
      return {
         "error": f"Measurement {slug} not found."
      }

   return measurement
```


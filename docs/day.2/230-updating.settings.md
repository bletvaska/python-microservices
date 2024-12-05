# Aktualizácia nastavení

Nastavenia aktualizujeme o časový interval, ktorý bude definovať interval sťahovania. Tento interval bude definovaný počtom minút alebo sekúnd (podľa dohody).

Aktualizovaná podoba nastavení bude teda vyzerať nasledovne:

```python
class Settings(BaseSettings):
    api_token: str | None = None
    interval: int = 60

    model_config = SettingsConfigDict(
        env_file_encoding='utf-8',
        env_file='.env',
        env_prefix='WEATHER_',
    )
```

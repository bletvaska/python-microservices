# Settings

Twelve factor app hovori, ze ten spravny sposob, ako drzat konfiguraciu aplikacie, ktora sa meni medzi jednotlivymi
deploymentmi, su premenne prostredia.

Podobne aj my budeme nastavenia aplikácie udržiavať v podobe premenných prostredia.


## Installation

Najprv nainstalujeme balik `pydantic-settings`:

```bash
$ poetry add "pydantic-settings"
```


## Settings Model

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    environment: str = 'production'
    db_uri: str = 'sqlite:///database.sqlite'
    api_token: str | None = None
```

exportnut premennu z prikazoveho riadku:

```bash
export DB_URI="do suboru"
```

vyskusat pomocou `ipython`:

```python
from weather.models.settings import Settings
settings = Settings()
settings.db_uri
# "do suboru"
```


## Citanie nastaveni z `.env` suboru

```python
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    environment: str = 'production'
    db_uri: str = 'sqlite:///database.sqlite'
    api_token: str | None = None

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        env_prefix='weather_'
    )
```

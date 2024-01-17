# Settings

Twelve factor app hovori, ze ten spravny sposob, ako drzat konfiguraciu aplikacie, ktora sa meni medzi jednotlivymi 
deploymentmi, su premenne prostredia.

Podobne aj my budeme nastavenia aplikácie udržiavať v podobe premenných prostredia.


## Installation

```bash
$ poetry add "pydantic[dotenv]"
```

## Settings Model

```python
from pydantic import AnyHttpUrl, BaseSettings, DirectoryPath


class Settings(BaseSettings):
    environment = "production"
    db_uri: str = "sqlite:///db.sqlite"
    slug_length = 5
    storage: DirectoryPath = 'storage/'
    # base_url: AnyHttpUrl = 'https://7aa6-88-212-39-249.eu.ngrok.io'
    base_url: AnyHttpUrl = 'http://localhost:9000'

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        env_prefix = "pokedex_"
```

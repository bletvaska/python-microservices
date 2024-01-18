from pydantic import HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    environment: str = 'production'
    db_uri: str = 'sqlite:///database.sqlite'
    api_token: str | None = None
    base_url: HttpUrl = 'http://localhost:8000'

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        env_prefix='weather_'
    )

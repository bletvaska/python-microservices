from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    api_token: str | None = None
    interval: int = 60
    db_uri: str = 'sqlite:///weather.sqlite'

    model_config = SettingsConfigDict(
        env_file_encoding='utf-8',
        env_file='.env',
        env_prefix='WEATHER_',
    )

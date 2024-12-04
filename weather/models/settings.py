from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    api_token: str | None = None

    model_config = SettingsConfigDict(
        env_file_encoding='utf-8',
        env_file='.env',
        env_prefix='WEATHER_',
    )

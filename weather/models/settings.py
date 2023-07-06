from pydantic import BaseSettings, AnyHttpUrl


class Settings(BaseSettings):
    db_uri: str = 'sqlite:///db.sqlite'
    environment = 'production'
    # base_url: AnyHttpUrl = 'http://localhost:8000'
    api_token: str = ''

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        env_prefix = 'weather_'

from functools import cache

from sqlmodel import create_engine

from .models.settings import Settings


@cache
def get_settings() -> Settings:
    print('>> Loading settings')
    return Settings()


@cache
def get_db_engine():
    print('>> Loading database engine')
    return create_engine(get_settings().db_uri)

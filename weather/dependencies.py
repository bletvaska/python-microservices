from functools import cache

from sqlalchemy import Engine
from sqlmodel import create_engine, Session

from .models.settings import Settings


@cache
def get_settings() -> Settings:
    print('>> Loading settings')
    return Settings()


@cache
def get_db_engine() -> Engine:
    print('>> Loading database engine')
    return create_engine(get_settings().db_uri)

def get_db_session() -> Session | None:
    with Session(get_db_engine()) as session:
        yield session

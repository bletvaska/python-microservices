from functools import cache

from loguru import logger
from sqlalchemy import Engine
from sqlmodel import create_engine, Session

from .models.settings import Settings


@cache
def get_settings() -> Settings:
    logger.info('Loading settings')
    return Settings()


@cache
def get_db_engine() -> Engine:
    logger.info('Loading database engine')
    return create_engine(get_settings().db_uri)

def get_db_session() -> Session | None:
    with Session(get_db_engine()) as session:
        yield session

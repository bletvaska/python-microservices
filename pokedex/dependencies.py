from functools import lru_cache
from pathlib import Path

from sqlmodel import Session, create_engine
from fastapi.templating import Jinja2Templates

from pokedex.models.settings import Settings


def get_session() -> Session:
    engine = create_engine(get_settings().db_uri)
    with Session(engine) as session:
        print('>> db connection created')
        yield session
        print('>> db connection closed')


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    print(f'Loading settings for: {settings.environment}.')
    return settings


@lru_cache
def get_jinja() -> Jinja2Templates:
    return Jinja2Templates(
        directory=Path(__file__).parent / 'templates'
    )

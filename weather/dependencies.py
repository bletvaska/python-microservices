from functools import lru_cache
from pathlib import Path

from loguru import logger
from sqlmodel import create_engine, Session
from fastapi.templating import Jinja2Templates

from weather.j2_filters import j2_strftime
from weather.models.settings import Settings


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    logger.info(f'Loading settings for {settings.environment} environment')
    return settings


def get_session():
    engine = create_engine(get_settings().db_uri)
    with Session(engine) as session:
        yield session


@lru_cache
def get_templates():
    templates = Jinja2Templates(
        directory=Path(__file__).parent / 'templates',
    )

    # add filters
    templates.env.filters['strftime'] = j2_strftime

    return templates

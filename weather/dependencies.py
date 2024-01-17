from functools import lru_cache

from loguru import logger

from weather.models.settings import Settings


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    logger.info(f'Loading settings for {settings.environment} environment')
    return settings

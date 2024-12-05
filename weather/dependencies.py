from functools import cache

from .models.settings import Settings


@cache
def get_settings() -> Settings:
    print('>> Loading settings')
    return Settings()

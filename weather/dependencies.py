from functools import cache

from .models.settings import Settings


@cache
def get_settings():
    print('>> Loading settings')
    return Settings()

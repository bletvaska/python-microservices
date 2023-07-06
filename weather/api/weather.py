import httpx
import requests
from fastapi import APIRouter, Depends

from weather.dependencies import get_settings
from weather.models.settings import Settings

router = APIRouter()


@router.get('/api/weather/{city}')
def get_weather(city: str, country: str | None = None, units: str = 'metric', format: str = 'json',
                settings: Settings = Depends(get_settings)):
    url = 'https://api.openweathermap.org/data/2.5/weather'
    payload = {
        'q': city,
        'units': units,
        'format': format,
        'appid': settings.api_token
    }

    response = httpx.get(url, params=payload)
    return response.json()

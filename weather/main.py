import httpx
from fastapi import FastAPI

from .dependencies import get_settings

app = FastAPI()


@app.get('/api/weather', description='get weather info for given city')
async def get_weather(city: str, units: str = 'metric'):
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'units': units,
        'appid': get_settings().api_token
    }
    response = httpx.get(url, params=params)
    return response.json()

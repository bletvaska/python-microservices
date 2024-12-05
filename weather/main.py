from http import HTTPStatus
from typing import Literal

import httpx
from fastapi import FastAPI, HTTPException

from .dependencies import get_settings

app = FastAPI()


@app.get('/api/weather', description='get weather info for given city')
async def get_weather(city: str, units: Literal['standard', 'metric', 'imperial'] = 'metric'):
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'units': units,
        'appid': get_settings().api_token
    }
    response = httpx.get(url, params=params)
    data = response.json()

    if response.status_code != HTTPStatus.OK:
        raise HTTPException(response.status_code, detail={
            'message': data['message'],
        })

    return data

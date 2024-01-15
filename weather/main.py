#!/usr/bin/env python3

import uvicorn
from fastapi import FastAPI
import httpx

app = FastAPI()


@app.get("/")
def hello():
    return "Hello, World!"


@app.get('/weather')
def get_weather(q: str = 'Kosice', units: str = 'metric', lang: str = 'en'):
    print('>> get weather')
    params = {
        'q': q,
        'units': units,
        'appid': '9e547051a2a00f2bf3e17a160063002d',
        'lang': lang
    }
    response = httpx.get('https://api.openweathermap.org/data/2.5/weather', params=params)
    return response.json()


def main():
    uvicorn.run('weather.main:app', reload=True, host='127.0.0.1', port=8000)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
import json

import uvicorn
from fastapi import FastAPI
import httpx
from fastapi_restful.tasks import repeat_every

app = FastAPI()


@app.get("/")
def hello():
    return "Hello, World!"


@app.get('/weather')
def get_weather():
    print('>> get weather')

    with open('weather.json') as file:
        return json.load(file)


@app.on_event("startup")
@repeat_every(seconds=20 * 60)
def retrieve_weather_data():
    print('>> retrieving')

    params = {
        'q': 'kosice',
        'units': 'metric',
        'appid': '9e547051a2a00f2bf3e17a160063002d',
        'lang': 'eng'
    }
    response = httpx.get('https://api.openweathermap.org/data/2.5/weather', params=params)

    with open('weather.json', 'w') as file:
        json.dump(response.json(), file, indent=2)


def main():
    uvicorn.run('weather.main:app', reload=True, host='127.0.0.1', port=8000)


if __name__ == '__main__':
    main()

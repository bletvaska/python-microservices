#!/usr/bin/env python3
import http
import json

from loguru import logger
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
    logger.info('Getting weather.')

    with open('weather.json') as file:
        return json.load(file)


@app.on_event("startup")
@repeat_every(seconds=20 * 60)
def retrieve_weather_data():
    logger.info('Retrieving weather data.')

    params = {
        'q': 'kosice',
        'units': 'metric',
        'appid': '9e547051a2a00f2bf3e17a160063002d',
        'lang': 'eng'
    }
    response = httpx.get('https://api.openweathermap.org/data/2.5/weatherx', params=params)

    if response.status_code == http.HTTPStatus.OK:
        with open('weather.json', 'w') as file:
            json.dump(response.json(), file, indent=2)
    else:
        logger.error(f'Data were not retrieved correctly. HTTP status code is {response.status_code}.')


def main():
    uvicorn.run('weather.main:app', reload=True, host='127.0.0.1', port=8000)


if __name__ == '__main__':
    main()

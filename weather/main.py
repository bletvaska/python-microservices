#!/usr/bin/env python3

import uvicorn
from fastapi import FastAPI
import httpx

app = FastAPI()


@app.get("/")
def hello():
    return "Hello, World!"


@app.get('/weather')
def get_weather():
    print('>> get weather')
    response = httpx.get('https://api.openweathermap.org/data/2.5/weather?q=kosice&appid=9e547051a2a00f2bf3e17a160063002d')
    return response


def main():
    uvicorn.run('weather.main:app', reload=True,
                host='127.0.0.1', port=8000)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
    return "Hello, World!"


def main():
    uvicorn.run('weather.main:app', reload=True,
                host='127.0.0.1', port=8000)


if __name__ == '__main__':
    main()

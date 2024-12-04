import httpx
import uvicorn
from fastapi import FastAPI

from .models.settings import Settings

app = FastAPI()


@app.get("/api/hello")
def hello():
    return "Hello, World!!"


@app.get('/api/weather')
async def get_weather(city: str, units: str = 'metric'):
    settings = Settings()
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'units': units,
        'appid': settings.api_token
    }
    response = httpx.get(url, params=params)
    return response.json()


def main():
    uvicorn.run('weather.main:app', reload=True,
                host='0.0.0.0', port=8000)


if __name__ == '__main__':
    main()

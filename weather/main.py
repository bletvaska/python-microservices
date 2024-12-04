import httpx
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/api/hello")
def hello():
    return "Hello, World!!"


@app.get('/api/weather')
async def get_weather():
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': 'kosice,sk',
        'appid': '9e547051a2a00f2bf3e17a160063002d'
    }
    response = httpx.get(url, params=params)
    return response.json()


def main():
    uvicorn.run('weather.main:app', reload=True,
                host='0.0.0.0', port=8000)


if __name__ == '__main__':
    main()

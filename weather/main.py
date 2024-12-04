import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
   return "Hello, World!"


def main():
   uvicorn.run('weather.main:app', reload=True,
               host='0.0.0.0', port=8000)


if __name__ == '__main__':
   main()


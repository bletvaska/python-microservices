import uvicorn as uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def homepage():
    """
    Returns homepage.
    """
    return {
        "message": "hello world"
    }


if __name__ == '__main__':
    uvicorn.run('python-microservices.main:app', reload=True, host='0.0.0.0', port=8000)

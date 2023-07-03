import uvicorn as uvicorn
from fastapi import FastAPI
from sqladmin import Admin
from sqlmodel import create_engine

app = FastAPI()

# db engine
engine = create_engine('sqlite:///home/mirek/Documents/kurzy/python-courses/python-microservices/resources/pokedex.sqlite')
admin = Admin(app, engine)


@app.get('/')
def homepage():
    """
    Returns homepage.
    """
    return {
        "message": "hello world"
    }


if __name__ == '__main__':
    uvicorn.run('pokedex.main:app', reload=True, host='0.0.0.0', port=8000)

import uvicorn
from sqlmodel import SQLModel

from .dependencies import get_db_engine

# create db schema
SQLModel.metadata.create_all(get_db_engine())

# start app
uvicorn.run('weather.main:app', reload=True,
            host='0.0.0.0', port=8000)

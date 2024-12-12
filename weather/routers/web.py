from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy import func
from sqlmodel import select, Session
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from ..dependencies import get_jinja, get_db_session
from ..models.measurement import Measurement

router = APIRouter()


@router.get('/hello', response_class=HTMLResponse)
def hello(jinja: Annotated[Jinja2Templates, Depends(get_jinja)]):
    template = jinja.get_template('hello.html')
    return template.render({
        'title': 'Weather App 2024.12',
    })


@router.get('/{city}', response_class=HTMLResponse)
def homepage(city: str,
             jinja: Annotated[Jinja2Templates, Depends(get_jinja)],
             session: Annotated[Session, Depends(get_db_session)]):
    # get measurement
    statement = select(Measurement).where(func.lower(Measurement.city) == city.lower()).order_by(Measurement.dt.desc())
    measurement = session.exec(statement).first()

    # render data
    template = jinja.get_template('homepage.html')
    return template.render({
    })


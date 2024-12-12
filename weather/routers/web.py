from typing import Annotated

from fastapi import APIRouter, Depends
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from ..dependencies import get_jinja

router = APIRouter()


@router.get('/hello', response_class=HTMLResponse)
def hello(jinja: Annotated[Jinja2Templates, Depends(get_jinja)]):
    template = jinja.get_template('hello.html')
    return template.render({
        'title': 'Weather App 2024.12',
    })

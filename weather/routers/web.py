from pathlib import Path

from fastapi import APIRouter
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

router = APIRouter()

@router.get('/hello', response_class=HTMLResponse)
def hello():
    templates = Jinja2Templates(directory=Path(__file__).parent.parent / 'templates')
    template = templates.get_template('hello.html')
    return template.render()

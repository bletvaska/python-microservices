from pathlib import Path

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()


@router.get('/')
def homepage(request: Request):
    context = {
        'request': request
    }
    templates = Jinja2Templates(directory=Path(__file__).parent.parent / 'templates')

    return templates.TemplateResponse('hello.html', context)

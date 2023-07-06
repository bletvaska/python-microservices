from fastapi import Request, APIRouter, Depends
from fastapi.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from weather.dependencies import get_jinja

router = APIRouter()


@router.get('/', response_class=HTMLResponse)
def homepage(request: Request,
             jinja: Jinja2Templates = Depends(get_jinja)):
    context = {
        'request': request,
        'title': 'Vitajte | Pokédex',
    }
    return jinja.TemplateResponse('home.tpl.html', context)

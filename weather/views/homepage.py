import pendulum
from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, select

from weather.dependencies import get_templates, get_session, get_settings
from weather.models.measurement import Measurement
from weather.models.settings import Settings

router = APIRouter()


@router.get('/')
def homepage(
    request: Request,
    settings: Settings = Depends(get_settings),
    session: Session = Depends(get_session),
    templates: Jinja2Templates = Depends(get_templates)
):
    # get last weather measurement
    statement = select(Measurement).order_by(Measurement.id.desc())
    measurement = session.exec(statement).first()

    # background image nr
    background_nr = pendulum.now().hour // 2 + 1

    context = {
        'request': request,
        'message': "najlepsia stranka na svete (RT 2025)",
        'now': pendulum.now(),
        'sunrise': measurement.sunrise,
        'sunset': measurement.sunset,
        'weather': measurement,
        'refresh': '45',
        'version': '2024.01',
        'environment': settings.environment,
        'background_nr': background_nr
    }

    return templates.TemplateResponse('current.weather.html', context)

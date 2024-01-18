import http
from datetime import datetime

from fastapi import APIRouter, Depends
from fastapi_pagination.links import Page
from fastapi.responses import JSONResponse
from fastapi_pagination.ext.sqlmodel import paginate
from sqlalchemy import func
from sqlmodel import Session, select
from sqlalchemy.exc import NoResultFound
from loguru import logger

from weather.dependencies import get_session
from weather.models.problemdetails import ProblemDetails
from weather.models.measurement import Measurement

router = APIRouter()


@router.get("/api/measurements", response_model=Page[Measurement])
def get_measurements(start_date: datetime | None = None,
                     end_date: datetime | None = None,
                     city: str | None = None,
                     session: Session = Depends(get_session)):
    statement = select(Measurement)

    if city is not None:
        statement = statement.where(func.lower(Measurement.city) == city.lower())

    if start_date is not None:
        statement = statement.where(Measurement.dt >= start_date)

    if end_date is not None:
        statement = statement.where(Measurement.dt < end_date)

    return paginate(session, statement)


@router.get('/api/measurements/last')
def get_last_measurement(session: Session = Depends(get_session)):
    statement = select(Measurement).order_by(Measurement.id.desc())
    return session.exec(statement).first()


@router.get('/api/measurements/{slug}')
def get_measurement(slug: int, session: Session = Depends(get_session)):
    try:
        statement = select(Measurement).where(Measurement.id == slug)
        return session.exec(statement).one()
    except NoResultFound:
        logger.warning(f"Measurement {slug} not found.")

        content = ProblemDetails(
            status=http.HTTPStatus.NOT_FOUND,
            title='Measurement not found',
            detail=f"Measurement {slug} not found.",
            instance=f'/api/mesurements/{slug}'
        )

        return JSONResponse(
            status_code=content.status,
            content=content.model_dump(),
            media_type='application/problem+json'
        )

# MeasurementOut -> pridat linku na zaznam
# * vytvorit
# pridat parametre do /measurements na ziskanie zaznamov v danom casovom rozsahu

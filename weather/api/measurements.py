from fastapi import APIRouter, Depends
from fastapi_pagination.links import Page
from fastapi_pagination.ext.sqlmodel import paginate
from sqlmodel import Session, select

from weather.dependencies import get_session
from weather.models.measurement import Measurement

router = APIRouter()


@router.get("/api/measurements", response_model=Page[Measurement])
def list_of_measurements(session: Session = Depends(get_session)):
    statement = select(Measurement)
    return paginate(session, statement)


@router.get('/api/measurements/last')
def get_last_measurement(session: Session = Depends(get_session)):
    statement = select(Measurement).order_by(Measurement.id.desc())
    return session.exec(statement).first()


@router.get('/api/measurements/{slug}')
def detail_measurement(slug: int, session: Session = Depends(get_session)):
    statement = select(Measurement).where(Measurement.id == slug)
    measurement = session.exec(statement).one_or_none()

    if measurement is None:
        return {
            "error": f"Measurement {slug} not found."
        }

    return measurement


# MeasurementOut -> pridat linku na zaznam
# * vytvorit
# pridat parametre do /measurements na ziskanie zaznamov v danom casovom rozsahu

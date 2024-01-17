from fastapi import APIRouter, Depends
from sqlmodel import create_engine, Session, select

from weather.dependencies import get_settings, get_session
from weather.models.measurement import Measurement

router = APIRouter()


@router.get("/api/measurements")
def get_all_measurements(session: Session = Depends(get_session)):
    statement = select(Measurement)
    # if city is not None:
    #     statement = statement.where(Measurement.city == city)

    return session.exec(statement).all()


@router.get('/api/measurements/last')
def get_last_measurement(session: Session = Depends(get_session)):
    statement = select(Measurement).order_by(Measurement.id.desc())
    return session.exec(statement).first()

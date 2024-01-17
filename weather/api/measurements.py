from fastapi import APIRouter
from sqlmodel import create_engine, Session, select

from weather.dependencies import get_settings
from weather.models.measurement import Measurement

router = APIRouter()


@router.get("/api/measurements")
def get_all_measurements():
    engine = create_engine(get_settings().db_uri)

    with Session(engine) as session:
        statement = select(Measurement)
        # if city is not None:
        #     statement = statement.where(Measurement.city == city)

        return session.exec(statement).all()


@router.get('/api/measurements/last')
def get_last_measurement():
    engine = create_engine(get_settings().db_uri)

    with Session(engine) as session:
        statement = select(Measurement).order_by(Measurement.id.desc())

        return session.exec(statement).first()

from fastapi import APIRouter
from sqlmodel import create_engine, Session, select

from weather.models.measurement import Measurement
from weather.models.settings import Settings

settings = Settings()
router = APIRouter()


@router.get("/api/measurements")
def get_all_measurements(city: str = None):
    engine = create_engine(settings.db_uri)

    with Session(engine) as session:
        statement = select(Measurement)
        if city is not None:
            statement = statement.where(Measurement.city == city)

        return session.exec(statement).all()


@router.get('/api/measurements/last')
def get_last_measurement():
    engine = create_engine(settings.db_uri)

    with Session(engine) as session:
        statement = select(Measurement).order_by(Measurement.id.desc())

        return session.exec(statement).first()

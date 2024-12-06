from datetime import date
from typing import Annotated

from fastapi import Depends, APIRouter
from sqlalchemy import func
from sqlmodel import select, Session

from ..dependencies import get_db_session
from ..models.measurement import Measurement

router = APIRouter()


@router.get('/{city}/last')
async def get_last_measurement(city: str,
                               session: Annotated[Session, Depends(get_db_session)]):
    statement = select(Measurement).where(func.lower(Measurement.city) == city.lower()).order_by(Measurement.dt.desc())
    return session.exec(statement).first()


@router.get('/{city}')
async def get_measurements(session: Annotated[Session, Depends(get_db_session)],
                           city: str,
                           start_date: date = None,
                           end_date: date = None):
    # SELECT * FROM measurement WHERE city=':city'
    statement = select(Measurement)

    if city is not None:
        statement = statement.where(func.lower(Measurement.city) == city.lower())

    if start_date is not None:
        statement = statement.where(Measurement.dt >= start_date)

    if end_date is not None:
        statement = statement.where(Measurement.dt < end_date)

    return session.exec(statement).all()

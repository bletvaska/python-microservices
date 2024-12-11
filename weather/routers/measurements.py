from datetime import date
from http import HTTPStatus
from typing import Annotated

from fastapi import Depends, APIRouter, Request
from fastapi_pagination.ext.sqlmodel import paginate
from fastapi_pagination.links import LimitOffsetPage
from sqlalchemy import func
from sqlmodel import select, Session

from ..dependencies import get_db_session
from ..models.measurement import Measurement
from ..responses import ProblemDetailsResponse

router = APIRouter()


@router.get('/{city}/last')
async def get_last_measurement(request: Request,
                               city: str,
                               session: Annotated[Session, Depends(get_db_session)]):
    statement = select(Measurement).where(func.lower(Measurement.city) == city.lower()).order_by(Measurement.dt.desc())
    measurement = session.exec(statement).first()

    if measurement is None:
        return ProblemDetailsResponse(
            status_code=HTTPStatus.NOT_FOUND,
            title='Measurement not found.',
            detail=f"City with name '{city}' does not exist.",
            instance=request.url.path,
        )

    return measurement


@router.get('/{city}', response_model=LimitOffsetPage[Measurement])
async def get_measurements(session: Annotated[Session, Depends(get_db_session)],
                           city: str,
                           start_date: date = None,
                           end_date: date = None):
    # SELECT * FROM measurement WHERE city=':city' AND dt >= ':start_date' AND dt < ':end_date'
    statement = select(Measurement).where(func.lower(Measurement.city) == city.lower())

    if start_date is not None:
        statement = statement.where(Measurement.dt >= start_date)

    if end_date is not None:
        statement = statement.where(Measurement.dt < end_date)

    return paginate(session, statement)

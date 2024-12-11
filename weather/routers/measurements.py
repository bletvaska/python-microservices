from datetime import date
from http import HTTPStatus
from typing import Annotated

from fastapi import Depends, APIRouter
from fastapi.responses import JSONResponse
from fastapi_pagination.ext.sqlmodel import paginate
from fastapi_pagination.links import LimitOffsetPage
from sqlalchemy import func
from sqlmodel import select, Session

from ..dependencies import get_db_session
from ..models.measurement import Measurement
from ..models.problem_details import ProblemDetails

router = APIRouter()


@router.get('/{city}/last')
async def get_last_measurement(city: str,
                               session: Annotated[Session, Depends(get_db_session)]):
    statement = select(Measurement).where(func.lower(Measurement.city) == city.lower()).order_by(Measurement.dt.desc())
    measurement = session.exec(statement).first()

    if measurement is None:
        content = ProblemDetails(
            status=HTTPStatus.NOT_FOUND,
            title='File not found',
            detail=f"File with slug '{city}' does not exist.",
            instance=f'/api/{city}/last'
        )

        return JSONResponse(
            status_code=content.status,
            media_type='application/problem+json',
            content=content.model_dump()
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

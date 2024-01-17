from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from weather.dependencies import get_session
from weather.models.measurement import Measurement
from weather.models.pager import Pager

router = APIRouter()


@router.get("/api/measurements")
def list_of_measurements(page: int = 1,
                         page_size: int = 20,
                         session: Session = Depends(get_session)):
    statement = (
        select(Measurement)
        .offset((page - 1) * page_size)
        .limit(page_size)
    )
    results = session.exec(statement).all()

    pager = Pager(
        first=f'http://localhost:8000/api/measurements?page=1&page_size={page_size}',
        results=list(results),
        count=len(results)
    )

    return pager


@router.get('/api/measurements/last')
def get_last_measurement(session: Session = Depends(get_session)):
    statement = select(Measurement).order_by(Measurement.id.desc())
    return session.exec(statement).first()

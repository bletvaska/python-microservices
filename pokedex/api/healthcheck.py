from pathlib import Path

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlmodel import Session

from pokedex.dependencies import get_session

router = APIRouter()


def _is_db_healthy(session: Session):
    return session is not None


def _static_folder_exists():
    path = Path(__file__).parent.parent / 'static'
    return path.exists()


@router.get('/healthz')
def healthcheck(session: Session = Depends(get_session)):
    db_state = _is_db_healthy(session)
    static_folder_state = _static_folder_exists()

    is_healthy = db_state and static_folder_state

    return JSONResponse(
        status_code=200 if is_healthy else 500,
        content={
            'isHealthy': is_healthy,
            'dbState': db_state,
            'staticFolderExist': static_folder_state
        }
    )

import http

from fastapi import APIRouter
from starlette.responses import JSONResponse

from weather.dependencies import get_session

router = APIRouter()


def is_disk_healthy():
    return get_session()


def is_db_healthy():
    return False


@router.head('/health')
@router.get("/health")
def healthcheck():
    disk = is_disk_healthy()
    db = is_db_healthy()

    if disk and db:
        status = http.HTTPStatus.OK
    else:
        status = http.HTTPStatus.INTERNAL_SERVER_ERROR

    return JSONResponse(
        status_code=status,
        content={
            'status': disk and db,
            'disk': disk,
            'database': db
        }
    )

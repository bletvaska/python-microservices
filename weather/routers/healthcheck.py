from http import HTTPStatus
from time import sleep

from fastapi import APIRouter
from loguru import logger
from starlette.responses import JSONResponse

router = APIRouter()


@router.get('/deadlock')
def deadlock():
    while True:
        logger.info('Working on')
        sleep(1)


@router.head('/healthcheck')
@router.get('/healthcheck')
def healthcheck():
    is_fs_ok = True
    is_db_ok = True
    result = is_fs_ok and is_db_ok

    if result == True:
        status = HTTPStatus.OK
    else:
        status = HTTPStatus.INTERNAL_SERVER_ERROR

    return JSONResponse(
        status_code=status,
        content={
            'fs': is_fs_ok,
            'db': is_db_ok,
            'status': result
        }
    )

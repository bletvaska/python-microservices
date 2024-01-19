from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def healthcheck():
    return {
        'status': 'ok'
    }

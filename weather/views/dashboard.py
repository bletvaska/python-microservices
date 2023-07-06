from fastapi import Request, APIRouter

router = APIRouter()


@router.get('/dashboard')
def dashboard(request: Request):
    return 'dashboard'

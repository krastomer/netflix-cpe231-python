from fastapi import APIRouter

router = APIRouter(
    prefix='/movie',
    tags=['Movie'],
    responses={404: {'description': 'Not found'}}
)

# @router.get('/')

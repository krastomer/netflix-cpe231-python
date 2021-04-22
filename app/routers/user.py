from ..dependencies import get_current_user
from app.models.user import User
from fastapi import APIRouter, Depends

router = APIRouter(
    prefix='/user',
    tags=['user'],
    responses={404: {'description': 'Not found'}}
)


@router.get('/me', response_model=User)
async def read_user_me(current_user: User = Depends(get_current_user)):
    return current_user

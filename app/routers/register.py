from fastapi.param_functions import Depends
from app.models.user import UserRegister
from typing import Optional
from fastapi import APIRouter

router = APIRouter(
    prefix='/register',
    tags=['register'],
    responses={404: {'description': 'Not found'}}
)


@router.post('/')
async def register(user: UserRegister):

    return {'detail': 'success'}

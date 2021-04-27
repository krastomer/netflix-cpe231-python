from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from ..configs import *
from app.models.token import Token

router = APIRouter(
    prefix='/token',
    tags=['Token'],
    responses={404: {'detail': 'not found'}}
)


@router.post('/', response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_db, form_data.username, form_data.password)
    if not user:
        raise incorrect_expection
    access_token_expires = timedelta(minutes=TOKEN_EXPIRES)
    access_token = create_access_token(
        data={'sub': user.email},
        expires_delta=access_token_expires
    )
    return {'access_token': access_token, 'token_type': 'bearer'}

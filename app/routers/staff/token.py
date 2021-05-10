from datetime import timedelta
from app.dependencies import authenticate_staff, create_access_token, get_db
from fastapi import APIRouter
from fastapi.param_functions import Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from app import exceptions, config

router = APIRouter(
    prefix='/staff',
    tags=['Staff - Token'],
    responses={404: {'description': 'Not found'}}
)


@router.post('/token')
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    staff = authenticate_staff(db, form_data.username, form_data.password)
    if not staff:
        raise exceptions.incorrect_expection
    access_token_expires = timedelta(minutes=config.TOKEN_EXPIRES)
    access_token = create_access_token(
        data={'sub': staff.email},
        expires_delta=access_token_expires
    )
    return {'access_token': access_token, 'token_type': 'bearer'}

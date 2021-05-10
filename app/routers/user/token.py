from sqlalchemy.orm.session import Session
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from app.models.token import Token
from app.dependencies import authenticate_user, create_access_token, get_db
from app import exceptions, config

router = APIRouter(
    prefix='/token',
    tags=['User - Token'],
    responses={404: {'description': 'Not found'}}
)


@router.post('/', response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise exceptions.incorrect_expection
    access_token_expires = timedelta(minutes=config.TOKEN_EXPIRES)
    access_token = create_access_token(
        data={'sub': user.email},
        expires_delta=access_token_expires
    )
    return {'access_token': access_token, 'token_type': 'bearer'}

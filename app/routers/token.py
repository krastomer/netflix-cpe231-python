from app.models.token import Token
from typing import Optional
from app.models.user import UserWithHash
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext
from datetime import timedelta, datetime
from jose import jwt
from ..dependencies import TOKEN_EXPIRES, SECRET_KEY, ALGORITHM, get_user, incorrect_expection, fake_db

router = APIRouter(
    prefix='/token',
    tags=['token'],
    responses={404: {'description': 'Not found'}}
)


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def authenticate_user(db, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = timedelta(minutes=15)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


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

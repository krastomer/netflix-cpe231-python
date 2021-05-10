from datetime import datetime, timedelta
from typing import Optional
from database.schemas import UserId
from database.crud import get_staff_password, get_user_from_token, get_user_password
from fastapi import Depends
from sqlalchemy.orm import Session
from database.database import SessionLocal
from passlib.context import CryptContext
from jose import jwt, JWTError
from . import config, exceptions
import pyrebase

pwd_context = CryptContext(schemes=['sha256_crypt'])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def hash_password(text: str):
    return pwd_context.hash(text)


async def get_current_user(token: str = Depends(config.oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, config.SECRET_KEY,
                             algorithms=[config.ALGORITHM])
        email: str = payload.get('sub')
        if email is None:
            raise exceptions.credentials_expection
    except JWTError:
        raise exceptions.credentials_expection
    user = get_user_from_token(db, email=email)
    if user is None:
        raise exceptions.credentials_expection
    return user


async def get_current_active_user(current_user: UserId = Depends(get_current_user)):
    if not current_user.next_billing:
        raise exceptions.inactive_exception
    if current_user.next_billing < datetime.now().date():
        raise exceptions.inactive_exception
    return current_user


async def get_storage():
    firebase = pyrebase.initialize_app(config.firebase_config)
    storage = firebase.storage()
    return storage


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def authenticate_user(db, email: str, password: str):
    user = get_user_password(db, email)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def authenticate_staff(db, email: str, password: str):
    user = get_staff_password(db, email)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = timedelta(minutes=15)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(
        to_encode, config.SECRET_KEY, algorithm=config.ALGORITHM)
    return encoded_jwt

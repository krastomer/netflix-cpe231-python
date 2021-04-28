from database.crud import get_user_by_email
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


async def get_current_user(token: str = Depends(config.oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, config.SECRET_KEY,
                             algorithms=[config.ALGORITHM])
        email: str = payload.get('sub')
        if email is None:
            raise exceptions.credentials_expection
    except JWTError:
        raise exceptions.credentials_expection
    user = get_user_by_email(db, email=email)
    if user is None:
        raise exceptions.credentials_expection
    return user


async def get_storage():
    firebase = pyrebase.initialize_app(config.firebase_config)
    storage = firebase.storage()
    return storage

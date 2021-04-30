from datetime import datetime
from database.schemas import UserId
from database.crud import get_user_from_token
from fastapi import Depends
from sqlalchemy.orm import Session
from database.database import SessionLocal
from passlib.context import CryptContext
from jose import jwt, JWTError
from . import config, exceptions
from cryptography.fernet import Fernet
import pyrebase

pwd_context = CryptContext(schemes=['sha256_crypt'])

fernet = Fernet(config.FERNET_KEY)


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

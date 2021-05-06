from datetime import timedelta
from app.routers.token import create_access_token
from sqlalchemy.orm.session import Session
from app.dependencies import get_current_user, get_db, hash_password
from database.crud import create_user, delete_user_db, get_user_password
from database.schemas import UserHash, UserId
from fastapi import APIRouter, Depends
from app.exceptions import database_exception
import re
from ..exceptions import emailvalid_exception, bademail_exception, badpassword_exception, badregister_exception
from .. import config

router = APIRouter(
    prefix='/user',
    tags=['User'],
    responses={404: {'description': 'Not found'}}
)


def check_email(email: str):
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    if re.search(regex, email):
        return True
    return False


@router.post('/register')
async def register_user(user: UserHash, db: Session = Depends(get_db)):
    if not check_email(user.email):
        raise bademail_exception
    if get_user_password(db, user.email):
        raise emailvalid_exception
    if len(user.password) < 8 or user.password.isnumeric():
        raise badpassword_exception
    user.password = hash_password(user.password)
    success = create_user(db, user)
    if not success:
        raise badregister_exception
    else:
        access_token_expires = timedelta(minutes=config.TOKEN_EXPIRES)
        access_token = create_access_token(
            data={'sub': user.email},
            expires_delta=access_token_expires
        )
        return {'success': success,
                'access_token': access_token,
                'token_type': 'bearer'}


@router.delete('/')
async def delete_user(user: UserId = Depends(get_current_user), db: Session = Depends(get_db)):
    v = delete_user_db(db=db, user_id=user.id_account)
    if not v:
        raise database_exception
    return {'success': True}

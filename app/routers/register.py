from sqlalchemy.orm.session import Session
from app.dependencies import get_db
from database.crud import create_user, get_user_password
from database.schemas import User
from fastapi import APIRouter, Depends
from ..exceptions import emailvalid_exception

router = APIRouter(
    prefix='/register',
    tags=['Register'],
    responses={404: {'description': 'Not found'}}
)


@router.post('/')
async def register_user(user: User, db: Session = Depends(get_db)):
    if get_user_password(db, user.email):
        raise emailvalid_exception

    success = create_user(db, user)
    return {'test': success}

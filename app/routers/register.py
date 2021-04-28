from sqlalchemy.orm.session import Session
from app.dependencies import get_db
from database.crud import get_user_by_email
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
    if get_user_by_email(db, user.email):
        raise emailvalid_exception
    return {'test': 'test'}

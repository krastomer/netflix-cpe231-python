from database.crud import set_user_payment, get_user_payment
from database.schemas import UserId
from app.dependencies import get_current_user, get_db
from fastapi import APIRouter, Depends
from app.models.payment import Payment
from sqlalchemy.orm import Session
from ..exceptions import badparameter_exception, inactive_exception

router = APIRouter(
    prefix='/payment',
    tags=['Payment'],
    responses={404: {'description': 'Not found'}}
)


@router.get('/')
async def get_payment(user: UserId = Depends(get_current_user), db: Session = Depends(get_db)):
    user_payment = get_user_payment(db=db, email=user.email)
    if not user_payment:
        raise inactive_exception
    return user_payment


@router.post('/')
async def set_payment(new_payment: Payment, user: UserId = Depends(get_current_user), db: Session = Depends(get_db)):
    if len(new_payment.card_number) != 16 or len(new_payment.phone_number) != 10:
        raise badparameter_exception
    result = set_user_payment(
        db=db, email=user.email, payment=new_payment)
    return {'success': True if result else False}

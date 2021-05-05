from datetime import datetime, timedelta
from app.models.payment import Payment
from sqlalchemy.orm import Session
from . import models, schemas


def create_user(db: Session, user: schemas.UserHash):
    try:
        content = models.User(
            email=user.email,
            password=user.password,
            phone_number=None,
            firstname=None,
            lastname=None,
            card_number=None,
            exp_date=None,
            security_code=None,
            next_billing=None,
            plan_id=None
        )
        db.add(content)
        db.commit()
        db.refresh(content)
        return True
    except:
        return False


def get_user_password(db: Session, email: str):
    user = db.query(models.User).filter(models.User.email == email).first()
    if user:
        return schemas.UserHash(email=user.email, password=user.password)
    return None


def get_user_from_token(db: Session, email: str):
    user = db.query(models.User).filter(models.User.email == email).first()
    if user:
        return schemas.UserId(email=user.email, id_account=user.id_account, next_billing=user.next_billing)
    return None


def get_user_payment(db: Session, email: str):
    user = db.query(models.User).filter(models.User.email == email).first()
    if user:
        return Payment(
            email=user.email,
            phone_number=user.phone_number,
            firstname=user.firstname,
            lastname=user.lastname,
            card_number=user.card_number,
            exp_date=user.exp_date,
            security_code=user.security_code,
            next_billing=user.next_billing,
            plan_id=user.plan_id
        )
    return None


def set_user_payment(db: Session, email: str, payment: Payment):
    try:
        db.query(models.User).filter(models.User.email == email).update(
            {
                models.User.phone_number: payment.phone_number,
                models.User.card_number: payment.card_number,
                models.User.firstname: payment.firstname,
                models.User.lastname: payment.lastname,
                models.User.exp_date: payment.exp_date,
                models.User.security_code: payment.security_code,
                models.User.plan_id: payment.plan_id,
                models.User.next_billing: datetime.now().date(
                ) + timedelta(days=30) if payment.plan_id else payment.next_billing
            }, synchronize_session=False)
        db.commit()
        return True
    except:
        return False


def get_user_viewer(db: Session, id_account: int):
    viewer = db.query(models.Viewer).filter(
        models.Viewer.id_account == id_account)
    viewer_list = []
    if viewer.count() != 0:
        for i in viewer:
            viewer_list.append(schemas.Viewer(
                id_viewer=i.id_viewer,
                pin_number=i.pin_number,
                name=i.name,
                is_kid=i.is_kid
            ))
        return viewer_list
    else:
        v = add_user_viewer(db, id_account, schemas.Viewer(
            name='You', is_kid=False))
        viewer_list.append(v)
    return viewer_list


def add_user_viewer(db: Session, id_account: int, viewer: schemas.Viewer):
    try:
        if viewer.pin_number:
            content = models.Viewer(
                pin_number=viewer.pin_number,
                id_account=id_account,
                name=viewer.name,
                is_kid=viewer.is_kid
            )
        else:
            content = models.Viewer(
                id_account=id_account,
                name=viewer.name,
                is_kid=viewer.is_kid
            )
        db.add(content)
        db.commit()
        db.refresh(content)
        return viewer
    except:
        return False


def delete_user_db(db: Session, viewer: int):
    v = db.query(models.Viewer).filter(
        models.Viewer.id_viewer == viewer).delete()
    db.commit()
    return v

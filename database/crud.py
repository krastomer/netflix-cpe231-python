from sqlalchemy.orm import Session
from . import models, schemas


def create_user(db: Session, user: schemas.User):
    try:
        content = models.User(
            email=user.email,
            password=user.password,
            phone_number=user.phone_number,
            firstname=user.firstname,
            lastname=user.lastname,
            card_number=user.card_number,
            exp_date=user.exp_date,
            security_code=user.security_code,
            next_billing=user.next_billing,
            plan_id=user.plan_id
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
        return schemas.UserId(email=user.email, id_account=user.id_account)
    return None

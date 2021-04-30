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
        return schemas.UserId(email=user.email, id_account=user.id_account)
    return None

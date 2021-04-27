from sqlalchemy.orm import Session

from database import models, schemas


def create_user(db: Session, user: schemas.User):
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
    )
    db.add(content)
    db.commit()
    db.refresh()
    return content

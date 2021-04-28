from sqlalchemy import Column, Integer, String

from .database import Base


class User(Base):
    __tablename__ = 'user'

    id_account = Column(Integer, primary_key=True,
                        nullable=False, autoincrement=True)
    email = Column(String, unique=True)
    password = Column(String, nullable=False)
    phone_number = Column(String, unique=True)
    firstname = Column(String)
    lastname = Column(String)
    card_number = Column(String)
    exp_date = Column(String)
    security_code = Column(String)
    next_billing = Column(String)
    plan_id = Column(String)

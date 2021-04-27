from datetime import date
from typing import Optional
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Dependency


SQLALCHEMY_DATABASE_URL = "sqlite:///./DBNetflix.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class User(Base):
    __tablename__ = "UserNetflix"

    id_account = Column(Integer, primary_key=True,
                        index=True, autoincrement=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    phone_number = Column(String, unique=True)
    firstname = Column(String)
    lastname = Column(String)
    card_number = Column(String, unique=True)
    exp_date = Column(String)
    security_code = Column(Integer)
    next_billing = Column(String)


class UserBase(BaseModel):
    id_account: Optional[int]
    email: str


class UserCreate(UserBase):
    password: str
    phone_number: str
    firstname: str
    lastname: str
    card_number: str
    exp_date: str
    security_code: int
    next_billing: str


user = UserCreate(
    email='kasama.pops@mail.kmutt.ac.th',
    password='password',
    phone_number='0000000000',
    firstname='Kasama',
    lastname='Thongsawang',
    card_number='1012351230',
    exp_date='2021-10-08',
    security_code=132,
    next_billing='2021-10-08'
)


def create_user(db: Session, user: UserCreate):
    db_user = User(
        email=user.email,
        password=user.password,
        phone_number=user.phone_number,
        firstname=user.firstname,
        lastname=user.lastname,
        card_number=user.card_number,
        exp_date=user.exp_date,
        security_code=user.security_code,
        next_billing=user.next_billing
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

# x = create_user(SessionLocal(), user=user)


x = get_user(SessionLocal(), email='kasama.pops@mail.kmutt.ac.th')

print('done')

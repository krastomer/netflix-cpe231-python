from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    email: str
    full_name: Optional[str] = None
    disabled: Optional[bool] = None


class UserWithHash(User):
    password: str


class UserRegister(BaseModel):
    email: str
    password: str
    phone_number: str
    card_firstname: str
    card_lastname: str
    expire_date: str
    ccv: str

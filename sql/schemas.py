from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class User(UserBase):
    password: str
    phone_number: Optional[str]
    firstname: Optional[str]
    lastname: Optional[str]
    card_number: Optional[str]
    exp_date: Optional[str]
    security_code: Optional[str]
    next_billing: Optional[int]
    plan_id: Optional[int]

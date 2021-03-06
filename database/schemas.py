from typing import Optional
from pydantic import BaseModel
from datetime import date


class UserBase(BaseModel):
    email: str


class UserHash(UserBase):
    password: str


class User(UserHash):
    phone_number: Optional[str]
    firstname: Optional[str]
    lastname: Optional[str]
    card_number: Optional[str]
    exp_date: Optional[str]
    security_code: Optional[str]
    next_billing: Optional[date]
    plan_id: Optional[int]


class UserId(UserBase):
    id_account: int
    next_billing: Optional[date]


class Viewer(BaseModel):
    id_viewer: Optional[int]
    pin_number: Optional[str]
    name: str
    is_kid: bool

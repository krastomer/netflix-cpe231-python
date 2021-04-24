from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    email: str
    full_name: Optional[str] = None
    disabled: Optional[bool] = None


class UserWithHash(User):
    password: str

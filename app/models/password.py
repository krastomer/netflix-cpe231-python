from pydantic import BaseModel


class Password(BaseModel):
    password: str


class PackPassword(Password):
    new_password: str

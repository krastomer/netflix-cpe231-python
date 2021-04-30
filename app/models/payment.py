from datetime import date
from typing import Optional
from pydantic import BaseModel


class Payment(BaseModel):
    phone_number: Optional[str]
    firstname: Optional[str]
    lastname: Optional[str]
    card_number: Optional[str]
    exp_date: Optional[str]
    security_code: Optional[str]
    next_billing: Optional[date]
    plan_id: Optional[int]

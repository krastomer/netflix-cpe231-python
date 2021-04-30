from datetime import date
from typing import Optional
from pydantic import BaseModel


class PaymentBase(BaseModel):
    phone_number: Optional[str]
    firstname: Optional[str]
    lastname: Optional[str]
    card_number: Optional[str]
    exp_date: Optional[str]
    security_code: Optional[str]
    plan_id: Optional[int]


class Payment(PaymentBase):
    next_billing: Optional[date]

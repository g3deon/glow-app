from datetime import datetime
from pydantic import BaseModel, Field
from src.lib.py_object_id import PyObjectId

class PaymentHistory(BaseModel):
    id: PyObjectId
    invoice_id : PyObjectId
    amount: float = Field(..., ge=0)
    method: int = Field(ge=1, le=3)
    payment_date: datetime
    status: int = Field(ge=1, le=3)
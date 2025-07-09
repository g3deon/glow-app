from datetime import datetime
from pydantic import BaseModel, Field
from src.lib.py_object_id import PyObjectId


# Here its gonna be the user model, in our case we're going to use pydantic.

class PaymentHistory(BaseModel):
    id: PyObjectId
    invoid_id : PyObjectId
    amout: float
    method: int = Field(ge=1, le=3) #1-tarjeta 2-efectivo 3-etc
    payment_date: datetime
    status: int = Field(ge=1, le=3) # 1-pagado, 2-pendiente, 3- fallido
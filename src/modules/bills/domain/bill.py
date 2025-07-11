from enum import IntEnum,auto
from typing import List
from pydantic import BaseModel, Field
from src.lib.py_object_id import PyObjectId

class BillStatus(IntEnum):
    ACTIVE = auto()
    INACTIVE = auto()

class Bills(BaseModel):
    id : PyObjectId
    user_id : PyObjectId
    stripe_invoice_id : str
    status : List[BillStatus] = Field(...)


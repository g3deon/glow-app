from datetime import datetime
from pydantic import BaseModel, Field
from src.lib.py_object_id import PyObjectId

class Invoice(BaseModel):
    id: PyObjectId
    client_id: PyObjectId
    date: datetime
    services: list[PyObjectId]
    notes: str = Field(min_length=10, max_length=1000)
    total: float

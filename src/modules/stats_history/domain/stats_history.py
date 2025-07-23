from datetime import date, datetime
from pydantic import BaseModel, Field
from src.lib.py_object_id import PyObjectId


class StatsHistory(BaseModel):
    id: PyObjectId = Field(default=None)
    user_id: PyObjectId = Field(default=None)
    total_invoiced_amount: float =Field(ge=0)
    total_paid_amount: float = Field(ge=0)
    total_unpaid_amount: float
    total_invoices_count: int = Field(ge=0)
    pending_invoices_count: int = Field(ge=0)
    completed_invoices_count: int = Field(ge=0)
    total_clients: int = Field(ge=0)
    start_date: datetime
    end_date: datetime


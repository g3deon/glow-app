from datetime import datetime
from typing import List
from pydantic import BaseModel, Field

from src.lib.py_object_id import PyObjectId


class Subscription(BaseModel):
    id : PyObjectId
    user_id : PyObjectId
    stripe_customer_id : str
    stripe_subscription_id : str
    status : List[int] = Field(ge=1, le=3)
    plan : List[int] = Field(ge=1, le=2)
    start_date: datetime
    end_date: datetime
    update_at: datetime
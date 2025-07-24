from typing import Optional

from pydantic import BaseModel, Field

from src.lib.py_object_id import PyObjectId


class Service(BaseModel):
    id: Optional[PyObjectId] = Field(default=None)
    name: str = Field(...,min_length=3, max_length=30)
    description: str = Field(min_length=10, max_length=1000)
    price: float = Field(..., ge=0)
    category_ids: list[PyObjectId]
    accent_color: int = Field(...,ge=0, le=16777215)
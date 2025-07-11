from pydantic import BaseModel, Field
from src.lib.py_object_id import PyObjectId

class Shop(BaseModel):
    id: PyObjectId
    user_id: PyObjectId
    name: str = Field(...,min_length=3, max_length=30)
    description: str = Field(min_length=10, max_length=1000)
    accent_color: int = Field(ge=0, le=16777215)

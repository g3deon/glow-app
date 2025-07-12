from pydantic import BaseModel, EmailStr, Field
from src.lib.py_object_id import PyObjectId

class Client(BaseModel):
    id: PyObjectId
    name : str = Field(...,min_length=3, max_length=30)
    email : EmailStr
    phone : str = Field(pattern=r"^\+\d{2} \(\d{3}\) \d{3}-\d{4}$")
from pydantic import BaseModel,Field,EmailStr
from typing import Optional
from src.lib.py_object_id import PyObjectId


class User(BaseModel):
    id: Optional[PyObjectId] = Field(default=None)
    username: str = Field(...,min_length=3, max_length=30,pattern=r"^[a-zA-Z0-9_]+$")
    display_name: str = Field(..., min_length=  3,max_length=40)
    email: EmailStr
    address: Optional[str] = Field(None, max_length=255)
    phone: str = Field(pattern=r"^\+\d{1,2} \(\d{3}\) \d{3}-\d{4}$")
    accent_color: int = Field(ge=0, le=16777215)
    flags: int
    hashed_password: str = Field(min_length=8)
from pydantic import BaseModel,Field,EmailStr
from typing import Optional

class User(BaseModel):
    id: int
    username: str = Field(...,min_length=3, max_length=30,pattern=r"^[a-zA-Z0-9_]+$")
    display_name: str = Field(..., min_length=3,max_length=255)
    email: EmailStr
    hashed_password: str
    phone: str = Field(pattern=r"^\+\d{2} \(\d{3}\) \d{3}-\d{4}$")
    accent_color: int = Field(ge=0,le=16777215)
    flags: int
    address: Optional[str] = Field(None, max_length=255)
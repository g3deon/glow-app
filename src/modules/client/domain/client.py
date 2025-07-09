from pydantic import BaseModel, EmailStr, Field
from src.lib.py_object_id import PyObjectId

# Here its gonna be the user model, in our case we're going to use pydantic.

class Client(BaseModel):
    id: PyObjectId
    email : EmailStr
    phone : str = Field(pattern=r"^\+\d{2} \(\d{3}\) \d{3}-\d{4}$")
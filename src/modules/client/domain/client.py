from bson import ObjectId
from pydantic import BaseModel

from src.lib.py_object_id import PyObjectId


# Here its gonna be the user model, in our case we're going to use pydantic.

class Client(BaseModel):
    id: PyObjectId
    email : str
    phone : str
    preference : str
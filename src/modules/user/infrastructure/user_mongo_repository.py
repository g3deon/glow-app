from typing import List

from src.lib.config.ext.mongo_config import MongoDB
from src.lib.py_object_id import PyObjectId
from src.modules.user.domain.user import User
from src.modules.user.domain.user_errors import UserCreationError, UserFindError
from src.modules.user.domain.user_repository import UserRepository


class MongoRepository(UserRepository):
    def __init__(self, db = MongoDB()):
        self.db = db

    async def create_user(self, user: User) -> str:
        try:
            inserted_user = await self.db.insert('users',user.model_dump(exclude=user.id))
            return inserted_user
        except UserCreationError:
            raise UserCreationError

    async def get_all(self) -> list[User]:
        try:
            users_from_db = await self.db.find_all('users', User)
            return users_from_db
        except UserFindError:
            raise UserFindError

    async def get_by_username(self, username: str) -> User:
        try:
            user = await self.db.find_one_with_value('users', 'username', username, User)
            return user
        except UserFindError:
            raise UserFindError

    async def get_by_id(self, user_id: PyObjectId) -> User:
        try:
            print(f"user_id type: {type(user_id)}")
            user_from_db = await self.db.find_one_with_value('users','_id', user_id, User)
            return user_from_db
        except UserFindError:
            raise UserFindError

    async def get_by_email(self, email: str) -> User:
        try:
            user_from_db = await self.db.find_one_with_value('users', 'email', email, User)
            return user_from_db
        except UserFindError:
            raise UserFindError


    async def delete(self, user_id: PyObjectId) -> bool:
        try:
            user_from_db = await self.db.delete_document('users', user_id)
            return user_from_db
        except UserFindError:
            raise UserFindError
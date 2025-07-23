from src.lib.security.password_hash import PassswordFunctions
from src.lib.config.ext.mongo_config import MongoConnection
from src.lib.py_object_id import PyObjectId
from src.modules.user.domain.user import User
from src.modules.user.domain.user_errors import UserCreationError, UserFindError
from src.modules.user.domain.user_repository import UserRepository

class UserMongoRepository(UserRepository):
    mongo_connection = MongoConnection('users')

    async def create(self, user: User) -> User:
        try:
                _id = await self.mongo_connection.create(user.model_dump())
                user.id = PyObjectId(_id)
                return user
        except UserCreationError as e:
            raise e

    async def get_all(self) -> dict:
            return await self.mongo_connection.get_all()

    async def get_by_username(self, username: str) -> dict:
           return await self.mongo_connection.find_one({'username': username})


    async def get_by_id(self, user_id: PyObjectId) -> dict:
        try:
               return await self.mongo_connection.find_one({'_id': user_id})
        except UserFindError:
            raise UserFindError

    async def get_by_email(self, email: str) -> dict:
        try:
                return await self.mongo_connection.find_one({'email': email})
        except UserFindError:
            raise UserFindError


    async def delete(self, user_id: PyObjectId) -> dict:
        try:
               return await self.mongo_connection.delete(user_id)
        except UserFindError:
            raise UserFindError
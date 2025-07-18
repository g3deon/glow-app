from src.lib.security.password_hash import PassswordFunctions
from src.lib.config.ext.mongo_config import MongoConnection
from src.lib.py_object_id import PyObjectId
from src.modules.user.domain.user import User
from src.modules.user.domain.user_errors import UserCreationError, UserFindError
from src.modules.user.domain.user_repository import UserRepository


class UserMongoRepository(UserRepository):

    async def create(self, user: User) -> User:
        try:
            async with MongoConnection('users') as mongo:
                _id = await mongo.create(user.model_dump())
                user_created = await mongo.find_one(_id)
                return user_created
        except UserCreationError as e:
            raise e

    async def get_all(self) -> list[User]:
        async with MongoConnection('users') as mongo:
            return await mongo.get_all()

    async def get_by_username(self, username: str) -> User:
       async with MongoConnection('users') as mongo:
           return await mongo.find_one({'username': username})


    async def get_by_id(self, user_id: PyObjectId) -> User:
        try:
            async with MongoConnection('users') as mongo:
               return await mongo.find_one({'_id': user_id})
        except UserFindError:
            raise UserFindError

    async def get_by_email(self, email: str) -> User:
        try:
            async with MongoConnection('users') as mongo:
                return await mongo.find_one({'email': email})
        except UserFindError:
            raise UserFindError


    async def delete(self, user_id: PyObjectId) -> dict:
        try:
            async with MongoConnection('users') as mongo:
               return await mongo.delete(user_id)
        except UserFindError:
            raise UserFindError
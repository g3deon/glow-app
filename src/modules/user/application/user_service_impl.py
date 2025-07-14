from src.lib.py_object_id import PyObjectId
from src.lib.security.password_hash import PassswordFunctions
from src.modules.user.domain.user import User
from src.modules.user.domain.user_errors import UserFindError
from src.modules.user.domain.user_repository import UserRepository


class UserService:
    def __init__(self, user_repository : UserRepository):
        self.user_repository = user_repository

    async def create(self, user: User) -> User:
        user.hashed_password = PassswordFunctions.hash_password(user.hashed_password)
        return await self.user_repository.create(user)


    async def get_all(self):
        return await self.user_repository.get_all()


    async def get_user_by_id(self, user_id: PyObjectId) -> User:
        return await self.user_repository.get_by_id(user_id)


    async def get_user_by_username(self, username: str) -> User:
        try:
            return await self.user_repository.get_by_username(username)
        except UserFindError as e:
            raise UserFindError(f"User {username} not found. Message: {e}")


    async def get_user_by_email(self, email: str) -> User:
        return await self.user_repository.get_by_email(email)


    async def delete(self, user_id: PyObjectId) -> dict:
        return await self.user_repository.delete(user_id)


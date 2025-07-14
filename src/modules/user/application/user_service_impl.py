from src.lib.py_object_id import PyObjectId
from src.modules.user.domain.user import User
from src.modules.user.domain.user_repository import UserRepository


class UserService:
    def __init__(self, user_repository : UserRepository):
        self.user_repository = user_repository

    async def create(self, user: User) -> User:
        return await self.user_repository.create(user)


    async def get_all(self):
        return await self.user_repository.get_all()


    async def get_user_by_id(self, user_id: PyObjectId) -> User:
        return await self.user_repository.get_by_id(user_id)


    async def get_user_by_username(self, username: str) -> User:
        return await self.user_repository.get_by_username(username)


    async def get_user_by_email(self, email: str) -> User:
        return await self.user_repository.get_by_email(email)


    async def delete(self, user_id: PyObjectId) -> bool:
        return await self.user_repository.delete(user_id)


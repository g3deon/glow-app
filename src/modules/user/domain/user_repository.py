from abc import ABC, abstractmethod

from src.lib.py_object_id import PyObjectId
from src.modules.user.domain.user import User


class UserRepository(ABC):

    @abstractmethod
    async def create(self, user: User) -> User:
        pass

    @abstractmethod
    async def get_all(self) -> list[User]:
        pass

    @abstractmethod
    async def get_by_id(self, user_id: PyObjectId) -> User:
        pass

    @abstractmethod
    async def get_by_username(self, username: str) -> User:
        pass

    @abstractmethod
    async def get_by_email(self, email: str) -> User:
        pass

    @abstractmethod
    async def delete(self, user_id: PyObjectId) -> dict:
        pass



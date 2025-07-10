from abc import ABC, abstractmethod

from src.modules.user.domain.user import User


class UserRepository(ABC):

    @abstractmethod
    async def create_user(self, user: User) -> User:
        pass

    @abstractmethod
    async def get_all(self):
        pass

    @abstractmethod
    async def get_user_by_id(self, user_id: str) -> User:
        pass

    @abstractmethod
    async def get_user_by_username(self, username: str) -> User:
        pass

    @abstractmethod
    async def get_user_by_email(self, email: str) -> User:
        pass

    @abstractmethod
    async def delete(self, user_id: str) -> bool:
        pass



from src.lib.config.ext.mongo_config import MongoDB
from src.modules.user.domain.user import User
from src.modules.user.domain.user_errors import UserCreationError
from src.modules.user.domain.user_repository import UserRepository


class MongoRepository(UserRepository):
    def __init__(self, db = MongoDB()):
        self.db = db

    async def create_user(self, user: User) -> str:
        try:
            await self.db.connect()
            inserted_user = await self.db.insert('users',user.model_dump())
            return inserted_user

        except UserCreationError:
            raise UserCreationError
        finally:
            await self.db.close()

    async def get_all(self):
        pass

    async def get_user_by_id(self, user_id: str) -> User:
        pass

    async def get_user_by_username(self, username: str) -> User:
        pass

    async def get_user_by_email(self, email: str) -> User:
        pass


    async def delete(self, user_id: str) -> bool:
        pass
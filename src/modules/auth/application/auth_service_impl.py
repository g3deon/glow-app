from src.modules.auth.domain.auth_errors import AuthCredentialsError
from src.modules.token.domain.token_repository import TokenRepository
from src.modules.user.domain.user_repository import UserRepository


class AuthServiceImpl:
    def __init__(self, user_repository: UserRepository, token_repository: TokenRepository):
        self.user_repository = user_repository
        self.token_repository = token_repository


    async def login(self, email:str, hashed_password:str)-> str:
        try:
            user = await self.user_repository.get_by_email(email)

        except AuthCredentialsError as e:
            raise e
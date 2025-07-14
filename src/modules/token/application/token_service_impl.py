from src.modules.token.domain.token_repository import TokenRepository


class TokenService:
    def __init__(self, token: TokenRepository):
        self.token = token

        #if the logic is extensive
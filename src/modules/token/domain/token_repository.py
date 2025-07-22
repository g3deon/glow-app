from abc import ABC, abstractmethod

class TokenRepository(ABC):

    @abstractmethod
    async def generate_token(self, _id : str) -> str:
        pass

    @abstractmethod
    async def decode_token(self, token) -> dict:
        pass

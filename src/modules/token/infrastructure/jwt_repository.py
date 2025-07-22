from dotenv import load_dotenv

from src.modules.token.domain.token import Token
from src.modules.token.domain.token_repository import TokenRepository
import jwt
import os

load_dotenv()
EXP = int(os.getenv('EXPIRATION'))
ALGORITHM = os.getenv('ALGORITHM')
SECRET = os.getenv('SECRET_KEY')

class JWT2Repository(TokenRepository):

    async def generate_token(self, _id: str) -> str:
        data = dict(Token(exp=EXP, sub=_id))
        token = jwt.encode(data, SECRET, algorithm=ALGORITHM)
        return token

    async def decode_token(self, token : str) -> dict:
        payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        return payload

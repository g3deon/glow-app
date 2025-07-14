import base64
from dotenv import load_dotenv
from joserfc.errors import DecodeError

from src.modules.token.domain.token import Token
from src.modules.token.domain.token_repository import TokenRepository
from joserfc import jwt
from joserfc.jwk import OctKey
import os


load_dotenv()

ALGORITHM = os.getenv('ALGORITHM')
ISS = os.getenv('ISSUER')
KEY = os.getenv('SECRET_KEY')
EXP = int(os.getenv('EXPIRATION'))
key_bytes = base64.urlsafe_b64decode(KEY)

class JWTRepository(TokenRepository):
    key = OctKey.import_key("my_very_secret_key_that_is_43_chars_long!")

    async def decode_token(self, token) -> dict:
        try:
            payload = jwt.decode(token,self.key)
            return dict(payload.claims)
        except DecodeError as e:
            raise Exception(f'Token is invalid {e}')

    async def generate_token(self, data: dict) -> str:
        to_encode = data.copy()
        header = {"alg": ALGORITHM,}
        claims_test = dict(Token(exp=EXP, data=to_encode))
        return jwt.encode(header, claims_test,self.key)


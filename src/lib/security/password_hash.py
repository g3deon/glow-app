from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError, InvalidHashError

ph = PasswordHasher()

class PassswordFunctions:

    @staticmethod
    def hash_password(password) -> str:
        hashed_password = ph.hash(password)
        return hashed_password

    @staticmethod
    def verify_password(password: str, hashed_password: str) -> bool:
        try:
            return ph.verify(hashed_password, password)
        except (VerifyMismatchError, InvalidHashError):
            return False
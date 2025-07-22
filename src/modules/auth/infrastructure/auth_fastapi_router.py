from fastapi import APIRouter, Depends, HTTPException
from src.modules.auth.application.auth_service_impl import AuthServiceImpl
from src.modules.auth.domain.auth_errors import AuthCredentialsError
from src.modules.token.infrastructure.jwt_repository import JWTRepository
from src.modules.user.infrastructure.user_mongo_repository import UserMongoRepository


def get_service():
    user_rep = UserMongoRepository()
    token_rep = JWTRepository()
    return AuthServiceImpl(user_rep, token_rep)

auth_routes = APIRouter(tags=["auth"])

@auth_routes.post('/login')
async def login(email: str, password: str, service : AuthServiceImpl = Depends(get_service)):
    try:
        return await service.login(email, password)
    except AuthCredentialsError as e:
        HTTPException(status_code=401, detail=e)
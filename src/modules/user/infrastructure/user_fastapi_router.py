from fastapi import APIRouter, Depends, HTTPException

from src.modules.user.application.user_service_impl import UserService
from src.modules.user.domain.user import User
from src.modules.user.domain.user_errors import UserCreationError
from src.modules.user.infrastructure.user_mongo_repository import MongoRepository

user_routes = APIRouter()


def get_user_service():
    repository = MongoRepository()
    return UserService(repository)

@user_routes.post('/create')
async def create_user(user : User,service: UserService = Depends(get_user_service)):
    try:
     return await service.create_user(user)
    except UserCreationError:
        raise HTTPException(status_code=404, detail=f"Error creating {user}")

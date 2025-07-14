from fastapi import APIRouter, Depends, HTTPException
from src.modules.user.application.user_service_impl import UserService
from src.modules.user.domain.user import User
from src.modules.user.domain.user_errors import UserCreationError, UserFindError
from src.modules.user.infrastructure.user_mongo_repository import MongoRepository

user_routes = APIRouter(tags=["Users"])


def get_user_service():
    repository = MongoRepository()
    return UserService(repository)

@user_routes.post('/create')
async def create_user(user : User,service: UserService = Depends(get_user_service)):
    try:
     return await service.create(user)
    except UserCreationError:
        raise HTTPException(status_code=404, detail=f"Error creating {user}")
@user_routes.get('/get/users')
async def get_users(service: UserService = Depends(get_user_service)):
    try:
        return await service.get_all()
    except UserFindError:
        raise HTTPException(status_code=404, detail=f"Error finding users")

@user_routes.get('/users/{user_id}')
async def get_by_id(user_id, service: UserService = Depends(get_user_service)):
    try:
        return await service.get_user_by_id(user_id)
    except UserFindError:
        raise HTTPException(status_code=404, detail=f"Error find user")

@user_routes.get('/users/username/{username}')
async def get_by_username(username : str, service: UserService = Depends(get_user_service)):
    try:
        return await service.get_user_by_username(username)
    except UserFindError:
        raise HTTPException(status_code=404, detail=f"Error finding user")
@user_routes.delete('/users/delete/{user_id}')
async def delete_user(user_id, service: UserService = Depends(get_user_service)):
    try:
        return await service.delete(user_id)
    except UserFindError:
        raise HTTPException(status_code=404, detail=f"Error finding user")

from fastapi import APIRouter, Depends, HTTPException
from src.modules.user.application.user_service_impl import UserService
from src.modules.user.domain.user import User
from src.modules.user.domain.user_errors import UserCreationError, UserFindError
from src.modules.user.infrastructure.user_mongo_repository import UserMongoRepository


class HttpUserRouter:
    def __init__(self):
        self.service = UserService(UserMongoRepository())
        self.router = APIRouter(tags=["Users"],prefix="/users",responses={404: {"Message": "Not found"}})
        self.register_routes()

    def register_routes(self):
        @self.router.get("/")
        async def get_users():
            try:
                return await self.service.get_all()
            except UserFindError as e:
                raise HTTPException(status_code=404, detail=e)

        @self.router.get('/{user_id}')
        async def get_by_id(user_id):
            try:
                return await self.service.get_user_by_id(user_id)
            except UserFindError:
                raise HTTPException(status_code=404, detail=f"Error find user")

        @self.router.get('/username/{username}')
        async def get_by_username(username : str):
            try:
                return await self.service.get_user_by_username(username)
            except UserFindError:
                raise HTTPException(status_code=404, detail=f"Error finding user")

        @self.router.get('/email/{email}')
        async def get_by_email(email : str):
            try:
                return await self.service.get_user_by_email(email)
            except UserFindError:
                raise HTTPException(status_code=404, detail=f"Error finding user")

        @self.router.post('/', status_code=201)
        async def create_user(user : User):
            try:
             return await self.service.create(user)
            except UserCreationError as e:
                raise HTTPException(status_code=400, detail=f"Error creating {e}")

        @self.router.delete('/{user_id}')
        async def delete_user(user_id):
            try:
                return await self.service.delete(user_id)
            except UserFindError:
                raise HTTPException(status_code=404, detail=f"Error finding user")

user_routes = HttpUserRouter().router



from fastapi import APIRouter, HTTPException
from starlette import status

from src.modules.category.application.category_service_impl import CategoryServiceImpl
from src.modules.category.domain.category import Category
from src.modules.category.infrastructure.category_mongo_repository import CategoryMongoRepository



class HttpCategoryRouter:
    def __init__(self):
        self.service = CategoryServiceImpl(CategoryMongoRepository())
        self.router = APIRouter(
            prefix="/categories",
            tags=["Category"],
            responses={404: {"Message": "Not found"}}
        )
        self.register_routes()

    def register_routes(self):

        @self.router.get('/')
        async def get_all():
            try:
                return await self.service.get_all()
            except HTTPException as e:
                raise HTTPException(status_code=404) from e

        @self.router.get('/{id}')
        async def get_by_id(_id):
            try:
                return await self.service.get_by_id(_id)
            except HTTPException as e:
                raise HTTPException(status_code=404) from e

        @self.router.post('/', status_code=201)
        async def create(category: Category):
            try:
                return await self.service.create(category)
            except HTTPException as e:
                raise HTTPException(status_code=400) from e

        @self.router.put('/update/{id}')
        async def update(category: Category, _id , update_fields: list[str]):
            try:
                return await self.service.update(_id, category, update_fields)
            except HTTPException as e:
                raise HTTPException(status_code=404) from e
            except Exception as e:
                raise HTTPException(status_code=400) from e

        @self.router.delete('/{id}')
        async def delete(_id):
            try:
                deleted = await self.service.delete(_id)
                if deleted:
                    return status.HTTP_204_NO_CONTENT
            except HTTPException as e:
                raise HTTPException(status_code=404) from e
            except Exception as e:
                raise HTTPException(status_code=404) from e

categories_routes = HttpCategoryRouter().router




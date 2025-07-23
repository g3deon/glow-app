from typing import List, Optional
from src.lib.config.ext.mongo_config import MongoConnection
from src.lib.py_object_id import PyObjectId
from src.modules.category.domain.category_repository import CategoryRepository
from src.modules.category.domain.category import Category


class CategoryMongoRepository(CategoryRepository):
    mongo_connection = MongoConnection('categories')
    async def get_all(self) -> dict:
            return await self.mongo_connection.get_all()

    async def get_by_id(self, identification: PyObjectId) -> dict:
            return await self.mongo_connection.find_one({'_id': identification})

    async def create(self, category: Category) -> Category:
        created_id = await  self.mongo_connection.create(category.model_dump())
        category.id = PyObjectId(created_id)
        return category

    async def update(self, identification: PyObjectId, category: Category, update_fields: List[str]) -> Optional[Category]:
            updated_service = await self.mongo_connection.update(category.model_dump(), identification, update_fields)
            return updated_service

    async def delete(self, identification: PyObjectId) -> bool:
            return await self.mongo_connection.delete(identification)

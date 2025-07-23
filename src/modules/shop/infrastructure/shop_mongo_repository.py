from typing import List, Optional
from src.lib.config.ext.mongo_config import MongoConnection
from src.lib.py_object_id import PyObjectId
from src.modules.shop.domain.shop_repository import ShopRepository
from src.modules.shop.domain.shop import Shop


class ShopMongoRepository(ShopRepository):
    mongo_connection = MongoConnection('shops')
    async def get_all(self) -> dict:
            return await self.mongo_connection.get_all()

    async def get_by_id(self, identification: PyObjectId) -> dict:
            return await self.mongo_connection.find_one({'_id': identification})

    async def create(self, shop: Shop) -> Shop:
        created_id = await  self.mongo_connection.create(shop.model_dump())
        shop.id = PyObjectId(created_id)
        return shop

    async def update(self, identification: PyObjectId, shop: Shop, update_fields: List[str]) -> Optional[Shop]:
            updated_service = await self.mongo_connection.update(shop.model_dump(), identification, update_fields)
            return updated_service

    async def delete(self, identification: PyObjectId) -> bool:
            return await self.mongo_connection.delete(identification)

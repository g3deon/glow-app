from typing import List, Optional
from src.lib.config.ext.mongo_config import MongoConnection
from src.lib.py_object_id import PyObjectId
from src.modules.service.domain.service import Service
from src.modules.service.domain.service_repository import ServiceRepository


class ServiceMongoRepository(ServiceRepository):
    mongo_connection = MongoConnection('services')
    async def get_all(self) -> dict:
            return await self.mongo_connection.get_all()

    async def get_by_id(self, identification: PyObjectId) -> dict:
            return await self.mongo_connection.find_one({'_id': identification})

    async def create(self, service: Service) -> Service:
        created_id = await  self.mongo_connection.create(service.model_dump())
        service.id = PyObjectId(created_id)
        return service

    async def update(self, identification: PyObjectId, service:Service, update_fields: list[str]) -> Optional[Service]:
            updated_service = await self.mongo_connection.update(service.model_dump(), identification, update_fields)
            return updated_service

    async def delete(self, identification: PyObjectId) -> bool:
            return await self.mongo_connection.delete(identification)

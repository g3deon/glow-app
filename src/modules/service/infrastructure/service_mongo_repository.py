
from typing import List, Optional

from src.lib.config.ext.mongo_config import MongoConnection
from src.lib.py_object_id import PyObjectId
from src.modules.service.domain.service import Service
from src.modules.service.domain.service_repository import ServiceRepository


class ServiceMongoRepository(ServiceRepository):
    async def get_all(self) -> list[Service]:
        async with MongoConnection('services') as mongo:
            return await mongo.get_all()

    async def get_by_id(self, identification: PyObjectId) -> Optional[Service]:
        async with MongoConnection('services') as mongo:
            return await mongo.find_one({'_id': identification})

    async def create(self, service: Service) -> Service:
        async with MongoConnection('services') as mongo:
            created_id = await  mongo.create(service.model_dump())
        service.id = created_id
        return service

    async def update(self, identification: PyObjectId, service:Service, update_fields: list[str]) -> Optional[Service]:
        async with MongoConnection('services') as mongo:
            updated_service = await mongo.update(service.model_dump(), identification, update_fields)
            return updated_service

    async def delete(self, identification: PyObjectId) -> bool:
        async with MongoConnection('services') as mongo:
            return await mongo.delete(identification)

from typing import Optional, Any, Coroutine

from src.lib.py_object_id import PyObjectId
from src.modules.service.domain.service import Service
from src.modules.service.domain.service_repository import  ServiceRepository


class ServiceImplementation:
    def __init__(self, service_repository: ServiceRepository):
        self.service_repository = service_repository

    async def get_all(self):
        return await self.service_repository.get_all()

    async def get_by_id(self, identification: PyObjectId):
        return await self.service_repository.get_by_id(identification)

    async def create(self, service: Service):
        return await self.service_repository.create(service)

    async def update(self, identification: PyObjectId, service: Service, update_field: list[str]) -> Service:
        return await self.service_repository.update(identification,service,update_field)

    async def delete(self, identification: PyObjectId):
        return await self.service_repository.delete(identification)



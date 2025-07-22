from abc import ABC, abstractmethod
from typing import Optional,List
from src.lib.py_object_id import PyObjectId
from src.modules.service.domain.service import Service

class ServiceRepository(ABC):

    @abstractmethod
    async def get_all(self) -> List[Service]:
        pass

    @abstractmethod
    async def get_by_id(self, identification: PyObjectId) -> Optional[Service]:
        pass

    @abstractmethod
    async def create(self, service: Service) -> Service:
        pass

    @abstractmethod
    async def update(self, identification: PyObjectId, service:Service, update_field: list[str]) -> Optional[Service]:
        pass

    @abstractmethod
    async def delete(self, identification: PyObjectId) -> bool:
        pass


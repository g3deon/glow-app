from abc import ABC, abstractmethod
from typing import List,Optional
from src.lib.py_object_id import PyObjectId
from src.modules.client.domain.client import Client

class ClientRepository(ABC):
    @abstractmethod
    async def get_all(self) -> List[Client]:
        pass

    @abstractmethod
    async def get_by_id(self, identification: PyObjectId) -> Optional[Client]:
        pass

    @abstractmethod
    async def create(self, client: Client) -> Client:
        pass

    @abstractmethod
    async def update(self, identification: PyObjectId, client:Client, update_field:list[str]) -> Optional[Client]:
        pass

    @abstractmethod
    async def delete(self, identification: PyObjectId) -> bool:
        pass
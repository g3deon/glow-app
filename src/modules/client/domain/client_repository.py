from abc import ABC, abstractmethod
from typing import List,Optional
from src.lib.py_object_id import PyObjectId
from src.modules.client.domain.client import Client

class ClientRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Client]:
        pass

    @abstractmethod
    def get_by_id(self, identification: PyObjectId) -> Optional[Client]:
        pass

    @abstractmethod
    def create(self, client: Client) -> Client:
        pass

    @abstractmethod
    def update(self, identification: PyObjectId, client:Client, update_field:list[str]) -> Optional[Client]:
        pass

    @abstractmethod
    def delete(self, identification: PyObjectId) -> bool:
        pass
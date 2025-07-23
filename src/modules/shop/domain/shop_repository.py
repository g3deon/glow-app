from abc import ABC,abstractmethod
from typing import List, Optional
from src.lib.py_object_id import PyObjectId
from src.modules.shop.domain.shop import Shop


class ShopRepository(ABC):
    @abstractmethod
    async def get_all(self) -> List[Shop]:
        pass

    @abstractmethod
    async def get_by_id(self, identification: PyObjectId) -> Optional[Shop]:
        pass

    @abstractmethod
    async def create(self, shop: Shop) -> Shop:
        pass

    @abstractmethod
    async def update(self, identification: PyObjectId, shop: Shop, update_field: list[str]) -> Optional[Shop]:
        pass

    @abstractmethod
    async def delete(self, identification: PyObjectId) -> bool:
        pass
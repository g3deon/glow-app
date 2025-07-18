from abc import ABC,abstractmethod
from typing import List, Optional
from src.lib.py_object_id import PyObjectId
from src.modules.category.domain.category import Category


class CategoryRepository(ABC):
    @abstractmethod
    async def get_all(self) -> List[Category]:
        pass

    @abstractmethod
    async def get_by_id(self, identification: PyObjectId) -> Optional[Category]:
        pass

    @abstractmethod
    async def create(self, category: Category) -> Category:
        pass

    @abstractmethod
    async def update(self, identification: PyObjectId, category: Category, update_field: list[str]) -> Optional[Category]:
        pass

    @abstractmethod
    async def delete(self, identification: PyObjectId) -> bool:
        pass
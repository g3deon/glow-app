from typing import Optional

from src.lib.py_object_id import PyObjectId
from src.modules.category.domain.category_repository import CategoryRepository
from src.modules.category.domain.category import Category

class CategoryServiceImplementation:
    def __init__(self, category_repository: CategoryRepository):
        self.category_repository = category_repository

    def get_all(self) -> list[Category]:
        return self.category_repository.get_all()

    def get_by_id(self, identification: PyObjectId) -> Optional[Category]:
        return self.category_repository.get_by_id(identification)

    def create(self, category: Category) -> Category:
        return self.category_repository.create(category)

    def update(self, identification: PyObjectId, category: Category, update_field: list[str]) -> Category:
        return self.category_repository.update(identification,category,update_field)

    def delete(self, identification: PyObjectId) -> bool:
        return self.category_repository.delete(identification)

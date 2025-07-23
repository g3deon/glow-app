from typing import Optional, Any, Coroutine
#todo delete the courtine

from src.lib.py_object_id import PyObjectId
from src.modules.shop.domain.shop_repository import ShopRepository
from src.modules.shop.domain.shop import Shop

class ShopServiceImpl:
    def __init__(self, shop_repository: ShopRepository):
        self.shop_repository = shop_repository

    def get_all(self) -> Coroutine[Any, Any, list[Shop]]:
        return self.shop_repository.get_all()

    def get_by_id(self, identification: PyObjectId) -> Coroutine[Any, Any, Shop | None]:
        return self.shop_repository.get_by_id(identification)

    def create(self, shop: Shop) -> Coroutine[Any, Any, Shop]:
        return self.shop_repository.create(shop)

    def update(self, identification: PyObjectId, shop: Shop, update_field: list[str]) -> Coroutine[
        Any, Any, Shop | None]:
        return self.shop_repository.update(identification,shop,update_field)

    def delete(self, identification: PyObjectId) -> Coroutine[Any, Any, bool]:
        return self.shop_repository.delete(identification)

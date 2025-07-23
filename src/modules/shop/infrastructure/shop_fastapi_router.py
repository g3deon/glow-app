from fastapi import APIRouter, HTTPException
from src.modules.shop.application.shop_service_impl import ShopServiceImpl
from src.modules.shop.domain.shop import Shop
from src.modules.shop.infrastructure.shop_mongo_repository import ShopMongoRepository



class HttpShopRouter:
    def __init__(self):
        self.shop = ShopServiceImpl(ShopMongoRepository())
        self.router = APIRouter(
            prefix="/shops",
            tags=["Shop"],
            responses={404: {"Message": "Not found"}}
        )
        self.register_routes()

    def register_routes(self):

        @self.router.get('/')
        async def get_all():
            try:
                return await self.shop.get_all()
            except HTTPException as e:
                raise HTTPException(status_code=404) from e

        @self.router.get('/{id}')
        async def get_by_id(_id):
            try:
                return await self.shop.get_by_id(_id)
            except HTTPException as e:
                raise HTTPException(status_code=404) from e

        @self.router.post('/', status_code=201)
        async def create(shop: Shop):
            try:
                return await self.shop.create(shop)
            except HTTPException as e:
                raise HTTPException(status_code=400) from e

        @self.router.put('/{id}')
        async def update(shop: Shop, _id, update_fields: list[str]):
            try:
                return await self.shop.update(_id, shop, update_fields)
            except HTTPException as e:
                raise HTTPException(status_code=404) from e

        @self.router.delete('/{id}')
        async def delete(_id):
            try:
                return await self.shop.delete(_id)
            except HTTPException as e:
                raise HTTPException(status_code=404) from e

shops_routes = HttpShopRouter().router



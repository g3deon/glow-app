from fastapi import APIRouter, HTTPException
from src.modules.client.application.client_service_impl import ClientServiceImpl
from src.modules.client.domain.client import Client
from src.modules.client.infrastructure.client_mongo_repository import ClientMongoRepository

class HttpClientRouter:
    def __init__(self):
        self.service = ClientServiceImpl(ClientMongoRepository())
        self.router = APIRouter(
            prefix="/clients",
            tags=["Client"],
            responses={404: {"Message": "Not found"}}
        )
        self.register_routes()

    def register_routes(self):

        @self.router.get('/')
        async def get_all():
            try:
                return await self.service.get_all()
            except HTTPException as e:
                raise HTTPException(status_code=404) from e

        @self.router.get('/{id}')
        async def get_by_id(_id):
            try:
                return await self.service.get_by_id(_id)
            except HTTPException as e:
                raise HTTPException(status_code=404) from e

        @self.router.post('/',status_code=201)
        async def create(client: Client):
            try:
                return await self.service.create(client)
            except HTTPException as e:
                raise HTTPException(status_code=400) from e

        @self.router.put('/{id}')
        async def update(client: Client, _id, update_fields: list[str]):
            try:
                return await self.service.update(_id, client, update_fields)
            except HTTPException as e:
                raise HTTPException(status_code=404) from e

        @self.router.delete('/{id}')
        async def delete(_id):
            try:
                return await self.service.delete(_id)
            except HTTPException as e:
                raise HTTPException(status_code=404) from e

client_routes = HttpClientRouter().router



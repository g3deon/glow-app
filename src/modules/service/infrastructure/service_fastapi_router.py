from fastapi import APIRouter, HTTPException
from src.modules.service.application.service_service_impl import ServiceImplementation
from src.modules.service.domain.service import Service
from src.modules.service.infrastructure.service_mongo_repository import ServiceMongoRepository



class HttpServiceRouter:
    def __init__(self):
        self.service = ServiceImplementation(ServiceMongoRepository())
        self.router = APIRouter(
            prefix="/services",
            tags=["Service"],
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

        @self.router.post('/', status_code=201)
        async def create(service: Service):
            try:
                return await self.service.create(service)
            except HTTPException as e:
                raise HTTPException(status_code=400) from e

        @self.router.put('/{id}')
        async def update(service: Service, _id, update_fields: list[str]):
            try:
                return await self.service.update(_id, service, update_fields)
            except HTTPException as e:
                raise HTTPException(status_code=404) from e

        @self.router.delete('/{id}')
        async def delete(_id):
            try:
                return await self.service.delete(_id)
            except HTTPException as e:
                raise HTTPException(status_code=404) from e

services_routes = HttpServiceRouter().router



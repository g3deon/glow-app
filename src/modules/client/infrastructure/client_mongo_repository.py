from typing import Optional, List

from src.lib.config.ext.mongo_config import MongoConnection
from src.lib.py_object_id import PyObjectId
from src.modules.client.domain.client import Client
from src.modules.client.domain.client_repository import ClientRepository


class ClientMongoRepository(ClientRepository):
    async def get_all(self) -> List[Client]:
        async with MongoConnection('clients') as mongo:
            return await mongo.get_all()

    async def get_by_id(self, identification: PyObjectId) -> Optional[Client]:
        async with MongoConnection('clients') as mongo:
            return await mongo.find_one({'_id': identification})

    async def create(self, client: Client) -> Client:
        async with MongoConnection('clients') as mongo:
            created_id = await mongo.create(client.model_dump())
            client.id = created_id
            return client

    async def update(self, identification: PyObjectId, client: Client, update_fields: list[str]) -> Optional[Client]:
        async with MongoConnection('clients') as mongo:
            updated_client = await mongo.update(client.model_dump(mode='python'), identification, update_fields)
            return updated_client

    async def delete(self, identification: PyObjectId) -> bool:
        async with MongoConnection('clients') as mongo:
            return await mongo.delete(identification)
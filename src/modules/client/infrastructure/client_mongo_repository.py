from typing import Optional, List
from src.lib.config.ext.mongo_config import MongoConnection
from src.lib.py_object_id import PyObjectId
from src.modules.client.domain.client import Client
from src.modules.client.domain.client_repository import ClientRepository


class ClientMongoRepository(ClientRepository):
    mongo_connection = MongoConnection('clients')
    async def get_all(self) -> dict:
            return await self.mongo_connection.get_all()

    async def get_by_id(self, identification: PyObjectId) -> dict:
            return await self.mongo_connection.find_one({'_id': identification})

    async def create(self, client: Client) -> Client:
            created_id = await self.mongo_connection.create(client.model_dump())
            client.id = PyObjectId(created_id)
            return client

    async def update(self, identification: PyObjectId, client: Client, update_fields: list[str]) -> Optional[Client]:
            updated_client = await self.mongo_connection.update(client.model_dump(mode='python'), identification, update_fields)
            return updated_client

    async def delete(self, identification: PyObjectId) -> bool:
            return await self.mongo_connection.delete(identification)

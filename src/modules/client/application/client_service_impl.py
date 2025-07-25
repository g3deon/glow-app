from src.lib.py_object_id import PyObjectId
from src.modules.client.domain.client_repository import ClientRepository
from src.modules.client.domain.client import Client

class ClientServiceImpl:
    def __init__(self, client_repository: ClientRepository):
        self.client_repository = client_repository

    async def get_all(self) -> list[Client]:
        return await self.client_repository.get_all()

    async def get_by_id(self, identification: PyObjectId) -> Client:
        return await self.client_repository.get_by_id(identification)

    async def create(self, client: Client) -> Client:
        return await self.client_repository.create(client)

    async def update(self, identification: PyObjectId, client: Client, update_field: list[str]) -> Client:
        return await self.client_repository.update(identification, client, update_field)

    async def delete(self, identification: PyObjectId) -> bool:
        return await self.client_repository.delete(identification)

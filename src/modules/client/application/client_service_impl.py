from src.lib.py_object_id import PyObjectId
from src.modules.client.domain.client_repository import ClientRepository
from src.modules.client.domain.client import Client

class ClientServiceImplementation:
    def __init__(self, client_repository: ClientRepository):
        self.client_repository = client_repository

    def get_all(self) -> list[Client]:
        return self.client_repository.get_all()

    def get_by_id(self, identification: PyObjectId) -> Client:
        return self.client_repository.get_by_id(identification)

    def create(self, client: Client) -> Client:
        return self.client_repository.create(client)

    def update(self, identification: PyObjectId, client: Client, update_field: list[str]) -> Client:
        return self.client_repository.update(identification, client, update_field)

    def delete(self, identification: PyObjectId) -> bool:
        return self.client_repository.delete(identification)

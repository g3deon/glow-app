from typing import Optional, Any, Coroutine

from src.lib.py_object_id import PyObjectId
from src.modules.service.domain.service import Service
from src.modules.service.domain.service_repository import Service_Repository


class ServiceImplementation:
    def __init__(self, service_repository: Service_Repository):
        self.service_repository = service_repository

    def get_all(self):
        return self.service_repository.get_all()

    def get_by_id(self, identification: PyObjectId):
        return self.service_repository.get_by_id(identification)

    def create(self, service: Service):
        return self.service_repository.create(service)

    def update(self, identification: PyObjectId, service: Service, update_field: list[str]) -> Coroutine[
        Any, Any, Service | None]:
        return self.service_repository.update(identification,service,update_field)

    def delete(self, identification: PyObjectId):
        return self.service_repository.delete(identification)



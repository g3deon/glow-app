from abc import ABC, abstractmethod
from typing import List,Optional
from src.lib.py_object_id import PyObjectId
from src.modules.invoice.domain.invoice import Invoice


class InvoiceRepository(ABC):
    @abstractmethod
    async def get_all(self) -> List[Invoice]:
        pass

    @abstractmethod
    async def get_by_id(self, identification: PyObjectId) -> Optional[Invoice]:
        pass

    @abstractmethod
    async def create(self, invoice: Invoice) -> Invoice:
        pass

    @abstractmethod
    async def update(self, identification: PyObjectId, invoice:Invoice, update_field:list[str]) -> Optional[Invoice]:
        pass

    @abstractmethod
    async def delete(self, identification: PyObjectId) -> bool:
        pass
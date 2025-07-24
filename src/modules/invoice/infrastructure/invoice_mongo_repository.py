from typing import Optional, List
from src.lib.config.ext.mongo_config import MongoConnection
from src.lib.py_object_id import PyObjectId
from src.modules.invoice.domain.invoice import Invoice
from src.modules.invoice.domain.invoice_repository import InvoiceRepository


class InvoiceMongoRepository(InvoiceRepository):
    mongo_connection = MongoConnection('invoices')

    async def get_all(self) -> dict:
            return await self.mongo_connection.get_all()

    async def get_by_id(self, identification: PyObjectId) -> dict:
            return await self.mongo_connection.find_one({'_id': identification})

    async def create(self, invoice: Invoice) -> Invoice:
            created_id = await self.mongo_connection.create(invoice.model_dump())
            invoice.id = PyObjectId(created_id)
            return invoice

    async def update(self, identification: PyObjectId, invoice: Invoice, update_fields: list[str]) -> Optional[Invoice]:
            updated_invoice = await self.mongo_connection.update(invoice.model_dump(mode='python'), identification, update_fields)
            return updated_invoice

    async def delete(self, identification: PyObjectId) -> bool:
            return await self.mongo_connection.delete(identification)

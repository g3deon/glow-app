from src.lib.py_object_id import PyObjectId
from src.modules.invoice.domain.invoice import Invoice
from src.modules.invoice.domain.invoice_repository import InvoiceRepository


class InvoiceServiceImpl:
    def __init__(self, invoice_repository: InvoiceRepository):
        self.invoice_repository = invoice_repository

    async def get_all(self) -> list[Invoice]:
        return await self.invoice_repository.get_all()

    async def get_by_id(self, identification: PyObjectId) -> Invoice:
        return await self.invoice_repository.get_by_id(identification)

    async def create(self, invoice: Invoice) -> Invoice:
        return await self.invoice_repository.create(invoice)

    async def update(self, identification: PyObjectId, invoice: Invoice, update_field: list[str]) -> Invoice:
        return await self.invoice_repository.update(identification, invoice, update_field)

    async def delete(self, identification: PyObjectId) -> bool:
        return await self.invoice_repository.delete(identification)

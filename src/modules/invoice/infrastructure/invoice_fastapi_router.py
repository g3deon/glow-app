from fastapi import APIRouter, HTTPException
from src.modules.invoice.domain.invoice import Invoice
from src.modules.invoice.application.invoice_service_impl import InvoiceServiceImpl
from src.modules.invoice.infrastructure.invoice_mongo_repository import InvoiceMongoRepository


class HttpInvoiceRouter:
    def __init__(self):
        self.service = InvoiceServiceImpl(InvoiceMongoRepository())
        self.router = APIRouter(
            prefix="/invoice",
            tags=["Invoice"],
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
        async def create(invoice: Invoice):
            try:
                return await self.service.create(invoice)
            except HTTPException as e:
                raise HTTPException(status_code=400) from e

        @self.router.put('/{id}')
        async def update(invoice: Invoice, _id, update_fields: list[str]):
            try:
                return await self.service.update(_id, invoice, update_fields)
            except HTTPException as e:
                raise HTTPException(status_code=404) from e

        @self.router.delete('/{id}')
        async def delete(_id):
            try:
                return await self.service.delete(_id)
            except HTTPException as e:
                raise HTTPException(status_code=404) from e

invoice_routes = HttpInvoiceRouter().router



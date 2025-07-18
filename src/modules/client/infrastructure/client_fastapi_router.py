

from fastapi import APIRouter, Depends, HTTPException

from src.modules.client.application.client_service_impl import ClientServiceImplementation
from src.modules.client.domain.client import Client
from src.modules.client.infrastructure.client_mongo_repository import ClientMongoRepository

client_routes = APIRouter(tags=["Client"])

def get_service():
    repository = ClientMongoRepository()
    return ClientServiceImplementation(repository)

@client_routes.post('/client/create')
async def create(client : Client, service : ClientServiceImplementation = Depends(get_service) ):
    try:
        return await service.create(client)
    except HTTPException as e:
        raise HTTPException(status_code=400) from e

@client_routes.get('/clients')
async def get_all(service : ClientServiceImplementation = Depends(get_service)):
    try:
        return await service.get_all()
    except HTTPException as e:
        raise HTTPException(status_code=404) from e

@client_routes.get('/client/{id}')
async def get_by_id(_id , service : ClientServiceImplementation = Depends(get_service)):
    try:
        return await service.get_by_id(_id)
    except HTTPException as e:
        raise HTTPException(status_code=404) from e
@client_routes.delete('/client/delete/{id}')
async def delete(_id,service : ClientServiceImplementation = Depends(get_service)):
    try :
        return await service.delete(_id)
    except HTTPException as e:
        raise HTTPException(status_code=404) from e

@client_routes.put('/update/{id}')
async def update(client: Client, _id ,update_fields : list[str], service : ClientServiceImplementation = Depends(get_service)):
    try:
        return await service.update(_id, client, update_fields)
    except HTTPException as e:
        raise HTTPException(status_code=404) from e




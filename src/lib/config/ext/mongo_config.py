import asyncio
from typing import List, Any

from bson import ObjectId
from fastapi import HTTPException
from pymongo import AsyncMongoClient
from dotenv import load_dotenv
import os

from pymongo.errors import PyMongoError

from src.lib.py_object_id import PyObjectId

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DATABASE")

class MongoDB:
    def __init__(self):
        if not MONGO_URI:
            raise Exception('Mongo URI not set')
        self.client = AsyncMongoClient(MONGO_URI)
        self.database = self.client[MONGO_DB]

    @staticmethod
    def parse_id(entity: dict[str, Any]) -> str:
        parsed_id = entity['id'] = str(entity.pop('_id'))
        return parsed_id

    async def connect(self):
        return await  self.client.aconnect()

    async def close(self):
        if self.client:
           return await self.client.close()

    async def insert(self, colletion : str , inserted_data : dict[str,any]) -> str:
        query = await self.database[colletion].insert_one(inserted_data)
        return str(query.inserted_id)

    async def find_all(self, collection: str, model):
        entities = []

        async for entity in self.database[collection].find():
            self.parse_id(entity)
            entities.append(model(**entity))
        if len(entities) < 1:
            raise HTTPException(status_code=404, detail='colletion Empty')
        return entities

    async def find_one_with_value(self, collection, value_to_find, value, model):
        try:
            if value_to_find == "_id" and not isinstance(value, ObjectId):
                value = ObjectId(str(value))

            found = await self.database[collection].find_one({value_to_find : value})
            if not found:
                raise ValueError('not found')
            print(found)
            found = dict(found)
            self.parse_id(found)
            result = model(**found)
            return result

        except Exception as e:
            raise HTTPException(status_code=404, detail=f'str(e) {value_to_find} {type(value)} not found ')

    async def delete_document(self, collection : str ,document_id: PyObjectId) -> bool:
        try:
            if  not isinstance(document_id, ObjectId):
                document_id = ObjectId(str(document_id))

            result = await self.database[collection].delete_one({'_id': document_id})
            if result.deleted_count == 1:
                return True
            else:
                return False
        except PyMongoError as e:

            print(f"Error al eliminar documento en '{collection}': {e}")
            return False

mongo_instance = MongoDB()

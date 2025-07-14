from typing import Any
from bson import ObjectId
from pymongo import AsyncMongoClient
from dotenv import load_dotenv
import os


load_dotenv()

class MongoConnection:
    def __init__(self,collection: str):
        uri = os.getenv("MONGO_URI")
        database = os.getenv("MONGO_DATABASE")
        client = AsyncMongoClient(uri)

        self.client = client
        self.collection = client[database][collection]

    @staticmethod
    def parse_id(entity: dict[str, Any]) -> str:
        parsed_id = entity['id'] = str(entity.pop('_id'))
        return parsed_id

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.client:
            await self.client.close()

    async def get_all(self, page: int = 1, page_size: int = 10, filter_query: dict = None)  -> dict:
        if page < 1:
            page = 1
        if page_size < 1 or page_size > 25:
            page_size = 10

        filter_query = filter_query or {}

        skip = (page -1) * page_size
        cursor =  self.collection.find(filter_query).skip(skip).limit(page_size)
        total_documents = await self.collection.count_documents(filter_query)
        docs = await cursor.to_list(length=page_size)
        total_pages = (total_documents + page_size - 1 ) // page_size

        for doc in docs:
            self.parse_id(doc)
        return {
            "total_pages": total_pages,
            "results": docs
        }

    async def create(self, inserted_data : dict[str,Any]) -> dict :
        result = await self.collection.insert_one(inserted_data)
        return {'_id': str(result.inserted_id)}

    async def find_by_query(self, query: dict) -> dict:
        try:
            if '_id' in query and isinstance(query["_id"],str):
                query["_id"] = ObjectId(query["_id"])
            result = await self.collection.find_one(query)
            self.parse_id(result)
            return result
        except Exception as e:
            raise e

    async def delete(self, _id)-> dict:
        if  isinstance(_id, str):
           _id = ObjectId(_id)
        result = await self.collection.delete_one({'_id': _id})

        if result.deleted_count == 1:
            return {"status": "success", "message": "Documento eliminado correctamente."}
        if result.deleted_count == 0:
            return {"status": "error", "message": "Documento no encontrado."}





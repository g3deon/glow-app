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

    async def create(self, inserted_data : dict[str,Any]) -> str :
        result = await self.collection.insert_one(inserted_data)
        return str(result.inserted_id)

    async def find_one(self, query: dict) -> dict:
            if '_id' in query and isinstance(query["_id"],str):
                query["_id"] = ObjectId(query["_id"])
            result = await self.collection.find_one(query)
            self.parse_id(result)
            return result

    async def delete(self, _id):
        if  isinstance(_id, str):
           _id = ObjectId(_id)
        result = await self.collection.delete_one({'_id': _id})

        if result.deleted_count == 0:
            raise ValueError ("status error")

        return True

    async def update(self, document: dict, _id, fields: list[str]):

        if isinstance(_id, str):
            _id = ObjectId(_id)


        if len(fields) <= 0:
            raise ValueError("no keys to update!")

        new_document = {}
        for key in document.keys():
            if key in fields:
                new_document[key] = document[key]
        await self.collection.update_one({'_id': _id}, {'$set': new_document})
        return new_document
import asyncio

from pymongo import AsyncMongoClient
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DATABASE")

class MongoDB:
    def __init__(self):
        if not MONGO_URI:
            raise Exception('Mongo URI not set')
        self.client = AsyncMongoClient(MONGO_URI)
        self.database = self.client[MONGO_DB]

    async def connect(self):
        return await self.client.aconnect()

    def close(self):
        if self.client:
             self.client.close()

    async def insert(self, colletion : str , inserted_data : dict[str,any]) -> str:
        query = await self.database[colletion].insert_one(inserted_data)
        return str(query.inserted_id)


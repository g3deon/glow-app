from datetime import datetime
from typing import Optional, List
from src.lib.config.ext.mongo_config import MongoConnection
from src.lib.py_object_id import PyObjectId
from src.modules.stats_history.domain.stats_history import StatsHistory
from src.modules.stats_history.domain.stats_history_repository import StatsHistoryRepository


class StatsMongoRepository(StatsHistoryRepository):
    mongo_connection = MongoConnection('stats_history')
    async def get_all(self) -> dict:
            return await self.mongo_connection.get_all()

    async def get_by_id(self, identification: PyObjectId) -> dict:
            return await self.mongo_connection.find_one({'_id': identification})

    async def get_by_period(self, identification: PyObjectId, start_date: datetime, end_date: datetime) -> dict:
        #todo
            pass

    async def create(self, history: StatsHistory) -> StatsHistory:
            created_id = await self.mongo_connection.create(history.model_dump())
            history.id = PyObjectId(created_id)
            return history

    async def update(self, identification: PyObjectId, history: StatsHistory, update_fields: list[str]) -> Optional[StatsHistory]:
            updated_client = await self.mongo_connection.update(history.model_dump(mode='python'), identification, update_fields)
            return updated_client

    async def delete(self, identification: PyObjectId) -> bool:
            return await self.mongo_connection.delete(identification)

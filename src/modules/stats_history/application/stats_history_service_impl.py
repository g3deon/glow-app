from datetime import datetime

from src.lib.py_object_id import PyObjectId
from src.modules.stats_history.domain.stats_history_repository import StatsHistoryRepository
from src.modules.stats_history.domain.stats_history import StatsHistory

class StatsServiceImpl:
    def __init__(self, stats_history_repository: StatsHistoryRepository):
        self.stats_history_repository = stats_history_repository

    async def get_all(self) -> list[StatsHistory]:
        return await self.stats_history_repository.get_all()

    async def get_by_id(self, identification: PyObjectId) -> StatsHistory:
        return await self.stats_history_repository.get_by_id(identification)

    async def get_by_period(self, identification: PyObjectId, start_date: datetime, end_date: datetime) -> StatsHistory:
        return await self.stats_history_repository.get_by_period(identification, start_date, end_date)

    async def create(self, history: StatsHistory) -> StatsHistory:
        return await self.stats_history_repository.create(history)

    async def update(self, identification: PyObjectId, history: StatsHistory, update_field: list[str]) -> StatsHistory:
        return await self.stats_history_repository.update(identification, history, update_field)

    async def delete(self, identification: PyObjectId) -> bool:
        return await self.stats_history_repository.delete(identification)

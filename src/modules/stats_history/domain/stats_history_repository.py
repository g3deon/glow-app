from abc import ABC, abstractmethod
from datetime import datetime
from typing import List,Optional
from src.lib.py_object_id import PyObjectId
from src.modules.stats_history.domain.stats_history import StatsHistory

class StatsHistoryRepository(ABC):
    @abstractmethod
    async def get_all(self) -> List[StatsHistory]:
        pass

    @abstractmethod
    async def get_by_period(self, identification: PyObjectId, start_date: datetime, end_date: datetime) -> Optional[StatsHistory]:
        pass

    @abstractmethod
    async def get_by_id(self, identification: PyObjectId) -> Optional[StatsHistory]:
        pass

    @abstractmethod
    async def create(self, history: StatsHistory) -> StatsHistory:
        pass

    @abstractmethod
    async def update(self, identification: PyObjectId, history: StatsHistory, update_field:list[str]) -> Optional[StatsHistory]:
        pass

    @abstractmethod
    async def delete(self, identification: PyObjectId) -> bool:
        pass
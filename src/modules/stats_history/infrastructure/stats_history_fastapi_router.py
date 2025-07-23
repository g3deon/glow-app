from fastapi import APIRouter, HTTPException
from src.modules.stats_history.application.stats_history_service_impl import StatsServiceImpl
from src.modules.stats_history.domain.stats_history import StatsHistory
from src.modules.stats_history.infrastructure.stats_history_mongo_repository import StatsMongoRepository



class HttpStatsRouter:
    def __init__(self):
        self.stats = StatsServiceImpl(StatsMongoRepository())
        self.router = APIRouter(
            prefix="/stats",
            tags=["Stats"],
            responses={404: {"Message": "Not found"}}
        )
        self.register_routes()

    def register_routes(self):

        @self.router.get('/')
        async def get_all():
            try:
                return await self.stats.get_all()
            except HTTPException as e:
                raise HTTPException(status_code=404) from e

        @self.router.get('/{id}')
        async def get_by_id(_id):
            try:
                return await self.stats.get_by_id(_id)
            except HTTPException as e:
                raise HTTPException(status_code=404) from e

        @self.router.get('')
        async def get_by_period():
            #todo
            pass


        @self.router.post('/', status_code=201)
        async def create(stats: StatsHistory):
            try:
                return await self.stats.create(stats)
            except HTTPException as e:
                raise HTTPException(status_code=400) from e

        @self.router.put('/{id}')
        async def update(stats: StatsHistory, _id, update_fields: list[str]):
            try:
                return await self.stats.update(_id, stats, update_fields)
            except HTTPException as e:
                raise HTTPException(status_code=404) from e

        @self.router.delete('/{id}')
        async def delete(_id):
            try:
                return await self.stats.delete(_id)
            except HTTPException as e:
                raise HTTPException(status_code=404) from e

stats_routes = HttpStatsRouter().router



from fastapi import FastAPI

from src.lib.config.ext.mongo_config import mongo_instance
from src.modules.user.infrastructure.user_fastapi_router import user_routes

app = FastAPI(title='Glow App')

app.include_router(user_routes)


@app.on_event("startup")
async def startup_event():
    await mongo_instance.connect()

@app.on_event("shutdown")
async def shutdown_event():
    await mongo_instance.close()
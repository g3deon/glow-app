from fastapi import FastAPI
from src.modules.user.infrastructure.user_fastapi_router import user_routes

app = FastAPI(title='Glow App')

app.include_router(user_routes)



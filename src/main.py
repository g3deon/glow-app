from fastapi import FastAPI
from src.modules.auth.infrastructure.auth_fastapi_router import  auth_routes
from src.modules.client.infrastructure.client_fastapi_router import client_routes
from src.modules.user.infrastructure.user_fastapi_router import user_routes

app = FastAPI(title='Glow App')

app.include_router(user_routes)

app.include_router(auth_routes)

app.include_router(client_routes)
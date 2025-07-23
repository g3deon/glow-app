from fastapi import FastAPI
from src.modules.auth.infrastructure.auth_fastapi_router import  auth_routes
from src.modules.category.infrastructure.category_fastapi_router import categories_routes
from src.modules.client.infrastructure.client_fastapi_router import  client_routes
from src.modules.service.infrastructure.service_fastapi_router import services_routes
from src.modules.shop.infrastructure.shop_fastapi_router import shops_routes
from src.modules.stats_history.infrastructure.stats_history_fastapi_router import stats_routes
from src.modules.user.infrastructure.user_fastapi_router import user_routes




app = FastAPI(title='Glow App')



app.include_router(user_routes)

app.include_router(auth_routes)

app.include_router(client_routes)

app.include_router(services_routes)

app.include_router(categories_routes)

app.include_router(stats_routes)

app.include_router(shops_routes)



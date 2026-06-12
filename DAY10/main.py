from fastapi import FastAPI
from routers.tasks import router

app = FastAPI(
    title="Task CRUD API"
)

app.include_router(router)
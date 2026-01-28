from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from app.api.routes.health import health_router
from app.api.routes.jobs import jobs_router
from app.infra.models import Base, engine

app = FastAPI()
app.include_router(health_router)
app.include_router(jobs_router)

# Attach middleware + instrumentation BEFORE the app starts
Instrumentator().instrument(app).expose(app, endpoint="/metrics")

@app.on_event("startup")
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
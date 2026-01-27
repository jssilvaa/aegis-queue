from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from app.api.routes.health import health_router
from app.api.routes.jobs import jobs_router

app = FastAPI()
app.include_router(health_router)
app.include_router(jobs_router)

# Attach middleware + instrumentation BEFORE the app starts
Instrumentator().instrument(app).expose(app, endpoint="/metrics")

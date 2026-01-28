from celery import Celery
from app.core.config import settings

celery_app = Celery(
    "aegis",
    broker=f"redis://{settings.redis_host}:{settings.redis_port}/0",
)
from celery import Celery
import os

celery = Celery(
    "aegis",
    broker=f"redis://{os.environ['REDIS_HOST']}:{os.environ['REDIS_PORT']}/0",
)

celery.autodiscover_tasks(["worker"])
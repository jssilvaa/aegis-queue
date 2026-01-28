import time
import os 
import sqlalchemy as sa
from sqlalchemy import create_engine 
from worker.celery_app import celery

DATABASE_URL = (
    f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}"
    f"@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
)

engine = create_engine(DATABASE_URL)

@celery.task(bind=True, autoretry_for=(Exception,), retry_backoff=3)
def process_job(self, job_id: str):
    with engine.begin() as conn: 
        conn.execute(
            sa.text("UPDATE jobs SET status='running' WHERE id = :id"), 
            {"id": job_id}
        )

    time.sleep(10)  # Simulate a long-running task

    with engine.begin() as conn: 
        conn.execute(
            sa.text("UPDATE jobs SET status='done', result='sucess' WHERE id = :id"), 
            {"id": job_id},
        )
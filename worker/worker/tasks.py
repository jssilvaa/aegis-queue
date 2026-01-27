from worker.celery_app import celery
import time

@celery.task(bind=True, autoretry_for=(Exception,), retry_backoff=3)
def process_job(self, job_id: str):
    # simulate work 
    time.sleep(5)
    # update DB, status done
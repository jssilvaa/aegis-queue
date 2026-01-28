import uuid
from fastapi import APIRouter, HTTPException, status
from app.infra.models import SessionLocal, Job
from app.infra.celery_client import celery_app

jobs_router = APIRouter()

@jobs_router.post("/jobs")
async def create_job():
    job_id = str(uuid.uuid4())

    async with SessionLocal() as session: 
        session.add(Job(id=job_id, status="queued"))
        await session.commit()
    
    celery_app.send_task("worker.tasks.process_job", args=[job_id])

    return {"job_id": job_id, "status": "queued"}

@jobs_router.get("/jobs/{job_id}")
async def get_job_status(job_id: str):
    async with SessionLocal() as session:
        job = await session.get(Job, job_id)

    if not job: 
        return {"error": "not found"}
    
    return {"job_id": job.id, "status": job.status, "result": job.result}
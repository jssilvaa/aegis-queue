from fastapi import APIRouter, HTTPException, status

jobs_router = APIRouter()

@jobs_router.post("/jobs")
async def create_job():
    return {"job_id": "id", "status": "queued"}

@jobs_router.get("/jobs/{job_id}")
async def get_job_status(job_id: str):
    return {"job_id": job_id, "status": "unknown"} 
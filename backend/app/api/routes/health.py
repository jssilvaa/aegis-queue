from fastapi import APIRouter, status, HTTPException
from app.infra.db import check_postgres
from app.infra.redis import check_redis

health_router = APIRouter() 

@health_router.get("/health") 
async def health():
    return {"status": "ok"}

@health_router.get("/ready")
async def readiness():
    try:
        await check_postgres()
        await check_redis()
    except Exception as e: 
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Service Unavailable",
        )
    return {"status": "ready"}

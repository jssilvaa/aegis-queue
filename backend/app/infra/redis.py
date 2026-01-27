import redis.asyncio as redis
from app.core.config import settings

async def check_redis():
    client = redis.Redis(
        host=settings.redis_host,
        port=settings.redis_port,
        socket_timeout=3,
    )
    await client.ping()
    await client.close() 



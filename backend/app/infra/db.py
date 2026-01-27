import asyncpg
from app.core.config import settings

async def check_postgres():
    conn = await asyncpg.connect(
        host=settings.postgres_host, 
        port=settings.postgres_port,
        user=settings.postgres_user,
        password=settings.postgres_password,
        database=settings.postgres_db,
        timeout=3,
    )
    await conn.close()

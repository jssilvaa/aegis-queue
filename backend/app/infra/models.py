import sqlalchemy as sa
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from app.core.config import settings

DATABASE_URL = (
  f"postgresql+asyncpg://{settings.postgres_user}:{settings.postgres_password}"
  f"@{settings.postgres_host}:{settings.postgres_port}/{settings.postgres_db}"
)

engine = create_async_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()

class Job(Base): 
  __tablename__ = "jobs"

  id = sa.Column(sa.String, primary_key=True)
  status = sa.Column(sa.String, nullable=False)
  result = sa.Column(sa.String)
  created_at = sa.Column(sa.DateTime, server_default=sa.func.now())
  updated_at = sa.Column(sa.DateTime, onupdate=sa.func.now())


from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings

# Create the database engine
engine = create_async_engine(settings.DATABASE_URL, echo=True)

# Create a session factory
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Dependency to get the database session
async def get_db():
    async with async_session() as session:
        yield session
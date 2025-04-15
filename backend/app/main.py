from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

from .models.user import Base
from .core.database import engine
from .api.endpoints.user import router as user_router

from backend.app.seed_users import seed_example_users

app = FastAPI()

# Create database tables
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    await seed_example_users()

@app.get("/")
async def root():
    return {"message": "Welcome to the O1 Database API"}

app.include_router(user_router, prefix="/users", tags=["users"])

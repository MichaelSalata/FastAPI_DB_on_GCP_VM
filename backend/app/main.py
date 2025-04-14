from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
from .models.user import Base
from .core.database import engine
from .api.endpoints.user import router as user_router

app = FastAPI()

# Create database tables
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

class User(BaseModel):
    id: int
    name: str
    email: str

# example DB
users_db: Dict[int, User] = {
    1: User(id=1, name="John Doe", email="john.doe@dadjokes.com"),
    2: User(id=2, name="Jane Smith", email="jane.smith@catmemes.org"),
    3: User(id=3, name="Bob Builder", email="bob.builder@fixit.com"),
    4: User(id=4, name="Alice Wonderland", email="alice@teaparty.net"),
    5: User(id=5, name="Charlie Chocolate", email="charlie@factory.cocoa"),
    6: User(id=6, name="Dora Explorer", email="dora@mapquest.io"),
    7: User(id=7, name="Tony Stark", email="tony@starkindustries.ai"),
    8: User(id=8, name="Bruce Wayne", email="bruce@batmail.com"),
    9: User(id=9, name="Sherlock Holmes", email="sherlock@deduction.uk"),
    10: User(id=10, name="Homer Simpson", email="homer@donutspringfield.com"),
}

@app.get("/")
async def root():
    return {"message": "Welcome to the O1 Database API"}

@app.get("/users", response_model=Dict[int, User])
async def get_users():
    return users_db

@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    user = users_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User {user_id} not found")
    return user

@app.post("/users", response_model=User)
async def create_user(user: User):
    if user.id in users_db:
        raise HTTPException(status_code=400, detail="User {user.id} already exists")
    users_db[user.id] = user
    return user

@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, updated_user: User):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    users_db[user_id] = updated_user
    return updated_user

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    del users_db[user_id]
    return {"message": "User {user_id} deleted"}

app.include_router(user_router, prefix="/users", tags=["users"])

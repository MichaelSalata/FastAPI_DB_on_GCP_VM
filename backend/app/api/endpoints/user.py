from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import get_db
from crud.user import get_user, create_user
from schemas.user import UserCreate, UserResponse

router = APIRouter()

@router.get("/{user_id}", response_model=UserResponse)
async def read_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/", response_model=UserResponse)
async def create_new_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await create_user(db, user)
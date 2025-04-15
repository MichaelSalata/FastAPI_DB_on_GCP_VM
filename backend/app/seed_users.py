from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from .models.user import User as UserModel
from .core.database import async_session

example_user_entries = [
    {"name": "John Doe", "email": "john.doe@dadjokes.com"},
    {"name": "Jane Smith", "email": "jane.smith@catmemes.org"},
    {"name": "Bob Builder", "email": "bob.builder@fixit.com"},
    {"name": "Alice Wonderland", "email": "alice@teaparty.net"},
    {"name": "Charlie Chocolate", "email": "charlie@factory.cocoa"},
    {"name": "Dora Explorer", "email": "dora@mapquest.io"},
    {"name": "Tony Stark", "email": "tony@starkindustries.ai"},
    {"name": "Bruce Wayne", "email": "bruce@batmail.com"},
    {"name": "Sherlock Holmes", "email": "sherlock@deduction.uk"},
    {"name": "Homer Simpson", "email": "homer@donutspringfield.com"},
]

async def seed_example_users():
    async with async_session() as session:
        async with session.begin():
            for user_data in example_user_entries:
                existing_user = await session.execute(
                    select(UserModel).where(UserModel.email == user_data["email"])
                )
                if not existing_user.scalar():
                    new_user = UserModel(**user_data)
                    session.add(new_user)
            await session.commit()
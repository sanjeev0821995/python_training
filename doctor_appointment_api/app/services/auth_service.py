from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import User
from app.security import hash_password, verify_password, create_token
from app.schemas import UserCreate

class AuthService:
    @staticmethod
    async def register(data: UserCreate, session: AsyncSession):
        exists = await session.scalar(select(User).where(User.email == data.email))
        if exists:
            raise HTTPException(400, "Email already registered")
        user = User(email=data.email, name=data.name, role=data.role, password_hash=hash_password(data.password))
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user

    @staticmethod
    async def login(email: str, password: str, session: AsyncSession):
        user = await session.scalar(select(User).where(User.email == email))
        if not user or not verify_password(password, user.password_hash):
            raise HTTPException(401, "Invalid credentials")
        return create_token(user.id, user.role.value)

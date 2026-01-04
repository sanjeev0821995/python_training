from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_session
from app.schemas import UserCreate, Token
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register")
async def register(data: UserCreate, session: AsyncSession = Depends(get_session)):
    return await AuthService.register(data, session)

@router.post("/login", response_model=Token)
async def login(email: str, password: str, session: AsyncSession = Depends(get_session)):
    token = await AuthService.login(email, password, session)
    return {"access_token": token, "token_type": "bearer"}

@router.post("/forgot-password")
async def forgot_password(email: str):
    return {"message": "Mock password reset initiated for " + email}

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database import get_db
from app.models import User, UserRole
from app.security import decode_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db),
):
    payload = decode_token(token)
    if not payload or "sub" not in payload:
        raise HTTPException(status_code=401, detail="Invalid token")

    stmt = select(User).where(User.id == int(payload["sub"]))
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(401, "User not found")

    return user


async def require_doctor(user=Depends(get_current_user)):
    if user.role != UserRole.doctor:
        raise HTTPException(403, "Doctor access required")
    return user


async def require_patient(user=Depends(get_current_user)):
    if user.role != UserRole.patient:
        raise HTTPException(403, "Patient access required")
    return user

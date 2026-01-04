from fastapi import Depends, HTTPException
from jose import jwt
from sqlalchemy import select
from app.config import settings
from app.database import get_session
from app.models import User, UserRole

async def get_current_user(token: str, session=Depends(get_session)) -> User:
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, settings.JWT_ALGORITHM)
        user_id = int(payload["sub"])
    except Exception:
        raise HTTPException(401, "Invalid token")

    from sqlalchemy import select
    user = await session.scalar(select(User).where(User.id == user_id))
    if not user:
        raise HTTPException(404, "User not found")
    return user

def require_role(role: UserRole):
    async def wrapper(user=Depends(get_current_user)):
        if user.role != role:
            raise HTTPException(403, "Forbidden")
        return user
    return wrapper

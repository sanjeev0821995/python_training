from fastapi import APIRouter, Depends
from app.services.appointment_service import AppointmentService
from app.schemas import AppointmentCreate
from app.deps import require_role
from app.models import UserRole
from app.database import get_session

router = APIRouter(prefix="/appointments", tags=["appointments"])

@router.post("")
async def book(
    data: AppointmentCreate,
    user=Depends(require_role(UserRole.patient)),
    session=Depends(get_session),
):
    return await AppointmentService.book(user.id, data, session)

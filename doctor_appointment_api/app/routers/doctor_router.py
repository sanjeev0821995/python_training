from fastapi import APIRouter, Depends
from app.services.doctor_service import DoctorService
from app.deps import require_role
from app.models import UserRole
from app.schemas import AvailabilityCreate
from app.database import get_session

router = APIRouter(prefix="/doctors", tags=["doctors"])

@router.get("")
async def list_doctors(session=Depends(get_session)):
    return await DoctorService.list_doctors(session)

@router.post("/availability")
async def add_availability(
    data: AvailabilityCreate,
    user=Depends(require_role(UserRole.doctor)),
    session=Depends(get_session),
):
    return await DoctorService.add_availability(user.id, data, session)

@router.get("/{id}/availability")
async def get_availability(id: int, session=Depends(get_session)):
    return await DoctorService.get_availability(id, session)

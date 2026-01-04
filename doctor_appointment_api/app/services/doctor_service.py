from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models import Availability, User, UserRole
from app.schemas import AvailabilityCreate

class DoctorService:
    @staticmethod
    async def list_doctors(session: AsyncSession):
        return (await session.scalars(select(User).where(User.role == UserRole.doctor))).all()

    @staticmethod
    async def add_availability(doctor_id: int, data: AvailabilityCreate, session: AsyncSession):
        slot = Availability(doctor_id=doctor_id, **data.model_dump())
        session.add(slot)
        await session.commit()
        await session.refresh(slot)
        return slot

    @staticmethod
    async def get_availability(doctor_id: int, session: AsyncSession):
        return (await session.scalars(select(Availability).where(Availability.doctor_id == doctor_id))).all()

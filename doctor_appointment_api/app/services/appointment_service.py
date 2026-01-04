from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Appointment
from app.schemas import AppointmentCreate

class AppointmentService:
    @staticmethod
    async def book(patient_id: int, data: AppointmentCreate, session: AsyncSession):
        conflict = await session.scalar(select(Appointment).where(
            Appointment.doctor_id == data.doctor_id,
            Appointment.start_time == data.start_time
        ))
        if conflict:
            raise HTTPException(400, "Slot already booked")
        appt = Appointment(patient_id=patient_id, **data.model_dump())
        session.add(appt)
        await session.commit()
        await session.refresh(appt)
        return appt

    @staticmethod
    async def cancel(appointment_id: int, patient_id: int, session: AsyncSession):
        appt = await session.get(Appointment, appointment_id)
        if not appt or appt.patient_id != patient_id:
            raise HTTPException(404, "Appointment not found")
        await session.delete(appt)
        await session.commit()

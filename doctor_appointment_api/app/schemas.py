from pydantic import BaseModel, EmailStr
from datetime import datetime
from app.models import UserRole

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    role: UserRole
    name: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    role: UserRole
    name: str
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class AvailabilityCreate(BaseModel):
    start_time: datetime
    end_time: datetime

class AppointmentCreate(BaseModel):
    doctor_id: int
    start_time: datetime
    end_time: datetime

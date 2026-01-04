from sqlalchemy import Column, Integer, String, Enum, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship
from app.database import Base
import enum


class UserRole(str, enum.Enum):
    doctor = "doctor"
    patient = "patient"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(Enum(UserRole), nullable=False)
    name = Column(String, nullable=False)

    # Doctor -> Availability slots
    availabilities = relationship(
        "Availability",
        back_populates="doctor",
        cascade="all, delete-orphan"
    )

    # Doctor -> Appointments they attend as doctor
    doctor_appointments = relationship(
        "Appointment",
        foreign_keys="Appointment.doctor_id",
        back_populates="doctor",
        cascade="all, delete-orphan"
    )

    # Patient -> Appointments they booked
    patient_appointments = relationship(
        "Appointment",
        foreign_keys="Appointment.patient_id",
        back_populates="patient",
        cascade="all, delete-orphan"
    )


class Availability(Base):
    __tablename__ = "availability"

    id = Column(Integer, primary_key=True)
    doctor_id = Column(Integer, ForeignKey("users.id"))
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)

    doctor = relationship("User", back_populates="availabilities")


class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True)
    doctor_id = Column(Integer, ForeignKey("users.id"))
    patient_id = Column(Integer, ForeignKey("users.id"))
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)

    __table_args__ = (
        UniqueConstraint("doctor_id", "start_time", name="uq_doctor_time"),
    )

    doctor = relationship(
        "User",
        foreign_keys=[doctor_id],
        back_populates="doctor_appointments"
    )

    patient = relationship(
        "User",
        foreign_keys=[patient_id],
        back_populates="patient_appointments"
    )

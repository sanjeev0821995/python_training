from fastapi import FastAPI
from app.database import Base, engine
from app.routers import auth_router, doctor_router, appointment_router

app = FastAPI(title="Doctor Appointment API")

@app.on_event("startup")
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(auth_router.router)
app.include_router(doctor_router.router)
app.include_router(appointment_router.router)

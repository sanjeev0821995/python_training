from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import check_db_connection

app = FastAPI(title="Beginner FastAPI Auth")

users_db = {}

class RegisterRequest(BaseModel):
    username: str
    password: str

class LoginRequest(BaseModel):
    username: str
    password: str

@app.get("/db-status")
def db_status():
    return {"status": check_db_connection()}

@app.post("/register")
def register(user: RegisterRequest):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="User already exists")

    users_db[user.username] = user.password
    return {"message": "User registered successfully"}

@app.post("/login")
def login(user: LoginRequest):
    if user.username not in users_db:
        raise HTTPException(status_code=404, detail="User not found")

    if users_db[user.username] != user.password:
        raise HTTPException(status_code=401, detail="Invalid password")

    return {"message": "Login successful"}

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from backend.utils.auth_utils import send_otp, verify_otp
import smtplib
from email.mime.text import MIMEText

router = APIRouter()

class LoginRequest(BaseModel):
    email: EmailStr

class VerifyRequest(BaseModel):
    email: EmailStr
    otp: str

# In-memory store for demo
otp_store = {}

@router.post("/login")
async def login(request: LoginRequest):
    otp = send_otp(request.email)
    otp_store[request.email] = otp
    # In real, send email
    return {"message": "OTP sent to email"}

@router.post("/verify")
async def verify(request: VerifyRequest):
    if otp_store.get(request.email) == request.otp:
        del otp_store[request.email]
        return {"message": "Verified", "token": "dummy_token"}
    raise HTTPException(status_code=400, detail="Invalid OTP")

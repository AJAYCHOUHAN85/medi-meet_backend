import secrets
from datetime import datetime, timedelta
from passlib.context import CryptContext
from fastapi_mail import FastMail, MessageSchema
from config import conf

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def generate_otp() -> str:
    return str(secrets.randbelow(1000000)).zfill(6)

async def send_otp_email(email: str, otp: str):
    message = MessageSchema(
        subject="Password Reset OTP",
        recipients=[email],
        body=f"Your OTP for password reset is: {otp}\nIt will expire in 10 minutes.",
        subtype="plain"
    )
    fm = FastMail(conf)
    await fm.send_message(message)
    

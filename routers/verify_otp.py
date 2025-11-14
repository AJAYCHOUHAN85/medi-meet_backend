from fastapi import APIRouter , Depends , HTTPException , status
from database import get_db
from sqlalchemy.orm import Session
from schemas import RequestPasswordReset , VerifyOTP ,ResetPassword
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from database import get_db
from models import User , PasswordResetToken
from utils.helper import generate_otp , send_otp_email , hash_password

router = APIRouter(prefix="/verify-otp" , tags=["otp-verification"])

# Verify OTP
@router.post("/verify-otp")
def verify_otp(payload: VerifyOTP, db: Session = Depends(get_db)):
    # token = db.query(PasswordResetToken).filter_by(email=payload.email, otp=payload.otp, is_used=False).first()
    token = db.query(PasswordResetToken).filter_by(otp=payload.otp, is_used=False).first()

    if not token or token.expires_at < datetime.utcnow():
        raise HTTPException(status_code=400, detail="Invalid or expired OTP")

    token.is_used = True
    db.delete(token)
    db.commit()
    return {"message": "OTP verified. You can now reset your password."}

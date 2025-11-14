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

router = APIRouter(prefix="/api" , tags=["forget_password"])




#  Request Password Reset
@router.post("/request-password-reset")
async def request_password_reset(payload: RequestPasswordReset, db: Session = Depends(get_db)):
    user = db.query(User).filter_by(email=payload.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    otp = generate_otp()
    expires_at = datetime.utcnow() + timedelta(minutes=10)

    token = PasswordResetToken(email=payload.email, otp=otp, expires_at=expires_at)
    db.add(token)
    db.commit()
    await send_otp_email(payload.email, otp)
    return {"message": "OTP sent to your email."}


# # Verify OTP
# @router.post("/verify-otp")
# def verify_otp(payload: VerifyOTP, db: Session = Depends(get_db)):
#     token = db.query(PasswordResetToken).filter_by(email=payload.email, otp=payload.otp, is_used=False).first()
#     if not token or token.expires_at < datetime.utcnow():
#         raise HTTPException(status_code=400, detail="Invalid or expired OTP")

#     token.is_used = True
#     db.commit()
#     return {"message": "OTP verified. You can now reset your password."}


# # Reset Password
# @router.post("/reset-password")
# def reset_password(payload: ResetPassword, db: Session = Depends(get_db)):
#     user = db.query(User).filter_by(email=payload.email).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")

#     user.hashed_password = hash_password(payload.new_password)
#     db.commit()
#     return {"message": "Password reset successfully."}

    




    
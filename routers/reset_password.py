from fastapi import APIRouter , Depends , HTTPException , status
from database import get_db
from sqlalchemy.orm import Session
from schemas import ResetPassword
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import User 
from utils.helper import hash_password

router = APIRouter(prefix="/api" , tags=["reset_password"])


# Reset Password
@router.post("/reset-password")
def reset_password(payload: ResetPassword, db: Session = Depends(get_db)):
    user = db.query(User).filter_by(email=payload.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.hashed_password = hash_password(payload.new_password)
    db.commit()
    return {"message": "Password reset successfully."}
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from models import Doctor, User
from schemas import DoctorCreate, DoctorResponse
from utils.auth import get_current_user

router = APIRouter(prefix="/doctor", tags=["Doctor"])

# @router.post("/register", response_model=DoctorResponse)
# def create_doctor_profile(
#     doctor: DoctorCreate,
#     db: Session = Depends(get_db),
#     current_user_id: int = Depends(get_current_user_id)
# ):
    
@router.post("/register", response_model=DoctorResponse)
def create_doctor_profile(
    doctor: DoctorCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    ...

    
    user = db.query(User).filter(User.id == current_user).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Prevent duplicate doctor profile
    existing_doctor = db.query(Doctor).filter(Doctor.user_id == current_user).first()
    if existing_doctor:
        raise HTTPException(status_code=400, detail="Doctor profile already exists")
    

    new_doctor = Doctor(
        user_id=current_user,
        specialization=doctor.specialization,
        experience=doctor.experience,
        description=doctor.description,
        fees=doctor.fees,
        certificate_pdf=doctor.certificate_pdf
    )

    user.role = "doctor"  # Update role

    db.add(new_doctor)
    db.commit()
    db.refresh(new_doctor)

    return new_doctor

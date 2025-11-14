from fastapi import APIRouter , Depends , HTTPException
from schemas import DocterApproved
from sqlalchemy.orm import Session
from database import get_db
from models import  Doctor
from utils.auth import  is_admin


router = APIRouter(prefix="/api" , dependencies=[Depends(is_admin)], tags=["doctor_verification"])


@router.put("/admin/doctor/{doctor_userid}/accept")
def accept_doctor(doctor_id: int, db: Session = Depends(get_db)):
    doctor = db.query(Doctor).filter(Doctor.user_id== doctor_id).first()
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    doctor.approved = True
    db.commit()
    db.refresh(doctor)
    return {"message": f"Doctor  status updated to complete", "doctor": doctor}


    

    

    



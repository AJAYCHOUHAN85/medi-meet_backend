from fastapi import APIRouter , Depends, HTTPException
from schemas import GetAllSlot
from database import get_db
from sqlalchemy.orm import Session
from models import DoctorSlot

router = APIRouter(prefix="/api", tags=["/get_all_doctor_slot"])

@router.post("/get_all_doctor_slot")
def get_all_doctor(data:GetAllSlot , db : Session = Depends(get_db)):

    slots = db.query(DoctorSlot).filter(DoctorSlot.doctor_id == data.doctor_id).all()

    if not slots:
        raise HTTPException(status_code=404, detail="No slots found for this doctor/date")

    result = []
    for s in slots:
        result.append({
            "slot_id": s.id,
            "start_time": s.start_time.strftime("%H:%M"),
            "end_time": s.end_time.strftime("%H:%M"),
            "is_booked": s.is_booked
        })

    return {"slots": result}
from fastapi import APIRouter , Depends ,HTTPException
from database import get_db 
from sqlalchemy.orm import Session
from models import DoctorSlot
from schemas import GetSlotId

router = APIRouter(prefix="/api" , tags=["/book_slot"])

@router.post("/book")
def book_selected_slot(data: GetSlotId, db: Session = Depends(get_db)):

    slot = db.query(DoctorSlot).filter(DoctorSlot.id == data.slot_id).first()

    if not slot:
        raise HTTPException(status_code=404, detail="Slot not found ")

    if slot.is_booked:
        raise HTTPException(status_code=400, detail="Slot already booked ")

    
    slot.is_booked = True
    db.commit()
    db.refresh(slot)

    return {
        "message": "Slot booked successfully",
        "slot_id": slot.id,
        "doctor_id": slot.doctor_id,
        "date": str(slot.date),
        "start_time": slot.start_time.strftime("%H:%M"),
        "end_time": slot.end_time.strftime("%H:%M")
    }

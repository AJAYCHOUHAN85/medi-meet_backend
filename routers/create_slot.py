from fastapi import APIRouter , Depends ,HTTPException , status
from sqlalchemy.orm import Session
from database import get_db
from models import DoctorSlot ,User
from schemas import SlotCreateRequest
from datetime import datetime, timedelta, date as dt_date
from utils.auth import get_current_user

router = APIRouter(prefix="/api" , tags=["doctor_slot"])


@router.post("/create_slot")
def create_slots(data: SlotCreateRequest, db: Session = Depends(get_db) ,current_user: User = Depends(get_current_user)):
    created_slots = []

    try:
        slot_date = datetime.strptime(data.date, "%Y-%m-%d").date()
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format (use YYYY-MM-DD)")

    for slot_range in data.availability:
        try:
            start_time = datetime.strptime(slot_range.start, "%H:%M")
            end_time = datetime.strptime(slot_range.end, "%H:%M")
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid time format (use HH:MM)")

        current = start_time
        while current + timedelta(minutes=data.slot_duration) <= end_time:
            slot = DoctorSlot(
                doctor_id=current_user,
                date=slot_date,
                start_time=current.time(),
                end_time=(current + timedelta(minutes=data.slot_duration)).time(),
                is_booked=False
            )
            db.add(slot)
            created_slots.append({
                "date": str(slot_date),
                "start_time": slot.start_time.strftime("%H:%M"),
                "end_time": slot.end_time.strftime("%H:%M")
            })
            current += timedelta(minutes=data.slot_duration)

    db.commit()
    return {"message": "Slots created successfully", "slots": created_slots}




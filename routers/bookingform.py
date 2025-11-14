from fastapi import APIRouter ,Depends
from schemas import BookingForm
from sqlalchemy.orm import Session
from models import BookingFormModel ,User
from database import get_db
from utils.auth import get_current_user

router = APIRouter(prefix="/api" , tags=["/Booking Form"])





@router.post("/booking_form")
def booking_form(data: BookingForm, db: Session = Depends(get_db) ,
                 current_user: User = Depends(get_current_user) ):

    new_form = BookingFormModel(
        user_id=current_user,
        doctor_id=data.doctor_id,
        name = data.name,
        disease = data.disease,
        description = data.description        
    )

    db.add(new_form)
    db.commit()
    db.refresh(new_form)

    return {"message": "Form submitted successfully"}

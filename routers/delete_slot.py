from fastapi import APIRouter, Depends, HTTPException, status
from database import get_db
from schemas import DeleteSlot
from models import DoctorSlot, User
from sqlalchemy.orm import Session
from utils.auth import get_current_user

router = APIRouter(prefix="/api", tags=["delete_slot"])


@router.delete("/delete_slot")
def delete_slot(
    data: DeleteSlot,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    existing_data = (
        db.query(DoctorSlot)
        .filter(
            (DoctorSlot.doctor_id == current_user) & (DoctorSlot.id == data.id)
        )
        .first()
    )
    existing_data = (
        db.query(DoctorSlot)
        .filter(
            DoctorSlot.id == data.id
        )
        .first()
    )

    if not existing_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Slot not found",
        )

    db.delete(existing_data)
    db.commit()

    return {"message": "Slot deleted successfully"}


# from fastapi import APIRouter ,Depends ,HTTPException ,status
# from database import get_db
# from schemas import DeleteSlot
# from models import DoctorSlot , User
# from sqlalchemy.orm import Session
# from utils.auth import get_current_user

# router = APIRouter(prefix="/delete_slot", tags=["delete_slot"])


# @router.delete("/delete_slot")
# def delete_slot(data:DeleteSlot , db : Session = Depends(get_db) , current_user: User = Depends(get_current_user)):
#     existing_data = db.query(DoctorSlot).filter((current_user == DoctorSlot.doctor_id) & (DoctorSlot.id == data.id))

#     if not existing_data :
#         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND , details="Data not found")
    

#     db.delete(existing_data)
#     db.commit()
#     db.close()

#     return {"message" :" delete successfuly"}

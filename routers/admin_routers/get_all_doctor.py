from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from models import Doctor

router = APIRouter(prefix="/api", tags=["get_all_doctor"])


@router.get("/get_all_doctor/")
def read_doctor(db: Session = Depends(get_db)):
    doctor = db.query(Doctor).all()
    return doctor
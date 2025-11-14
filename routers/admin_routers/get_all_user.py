
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from models import User

router = APIRouter(prefix="/api", tags=["get_all_user"])


@router.get("/get_all_users/")
def read_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users
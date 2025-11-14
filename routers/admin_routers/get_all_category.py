from fastapi import APIRouter , Depends 
from sqlalchemy.orm import Session
from  database import get_db
from models import Category



router = APIRouter(prefix="/api" , tags=["get_category"])

@router.get("/get_all_category")
def get_all_category(db : Session = Depends(get_db)):
    all_category = db.query(Category).all()
    return all_category



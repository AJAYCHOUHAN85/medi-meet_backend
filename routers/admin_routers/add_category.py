from fastapi import APIRouter , Depends ,  HTTPException , status
from sqlalchemy.orm import Session
from models import Category
from schemas import CreateCategory

from database import get_db



router = APIRouter(prefix="/add_category" , tags=["add_category"])
@router.post("/add_category")
def add_category(data: CreateCategory, db: Session = Depends(get_db)):
    existing_data = db.query(Category).filter(Category.category_name == data.category_name).first()

    if existing_data:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="category_exist")

    db_category = Category(category_name=data.category_name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)

    return {"message": "Category added successfully"}




from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Category
from schemas import CreateCategory
from database import get_db

router = APIRouter(prefix="/delete_category", tags=["delete_category"])


@router.delete("/delete_category")
def delete_category( data : CreateCategory,
    db: Session = Depends(get_db)
):
    category = db.query(Category).filter(Category.category_name == data.category_name).first()

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    db.delete(category)
    db.commit()
    db.close()

    return {"message": "category has been deleted successfully"}
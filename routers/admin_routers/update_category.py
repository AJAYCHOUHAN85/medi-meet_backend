from fastapi import APIRouter , Depends , HTTPException , status
from sqlalchemy.orm import Session
from database import get_db
from schemas import CategoryUpdate
from models import Category


router = APIRouter(prefix="/api", tags=["update_category"])

@router.put("/{category_id}")
def update_category(category_id: int, data: CategoryUpdate, db: Session = Depends(get_db)):
    
    category = db.query(Category).filter(Category.id == category_id).first()

    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found"
        )

    if data.category_name:
        category.category_name = data.category_name

    db.commit()
    db.refresh(category)

    return {"message": "Category name updated successfully", "category": category.category_name}


    


    
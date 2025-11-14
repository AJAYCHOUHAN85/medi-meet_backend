from fastapi import APIRouter , Depends , HTTPException 
from sqlalchemy.orm import Session

from models import User
from utils.auth import get_current_user_data

from database import get_db
from schemas import UserUpdate


router = APIRouter(prefix="/api" , tags=["edit_user_profile"])



@router.put("/edit_profil")
def edit_profile(
    user_data : UserUpdate ,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user_data),
  
):
    profile_data = db.query(User).filter(User.id == user.id).first()

    if not profile_data:
        raise HTTPException(status_code=404, detail="User not found")
    
    if user_data.name is not None:
        profile_data.name = user_data.name


    if user_data.email is not None:
        profile_data.email = user_data.email

    if user_data.city is not None:
        profile_data.city = user_data.city

    if user_data.phone_no is not None:
        profile_data.phone_no = user_data.phone_no


    db.commit()
    db.refresh(profile_data)
    db.close()


    return{
        "message":"edit successfuly"
    }


    

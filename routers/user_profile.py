from fastapi import APIRouter , Depends , HTTPException 
from models import User


router = APIRouter(prefix="/user" , tags=["user-profile"])
from utils.auth import get_current_user_data

@router.get("/users_profile/")
def get_profile(current_user : User = Depends(get_current_user_data)):
    return{
        "id" : current_user.id,
        "name" : current_user.name,
        "email" : current_user.email,
        "phone_no": current_user.phone_no,
        "city" : current_user.city

    }


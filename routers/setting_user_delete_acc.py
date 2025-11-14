
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import User
from utils.auth import get_current_user_data
from database import get_db

router = APIRouter(prefix="/api", tags=["delete_account"])


@router.delete("/delete_account")
def delete_account(
    user: User = Depends(get_current_user_data),
    db: Session = Depends(get_db)
):
    account = db.query(User).filter(User.id == user.id).first()

    if not account:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(account)
    db.commit()
    db.close()

    return {"message": "Account has been deleted successfully"}

# @router.delete("/delete_account")
# def delete_account(
#     current_user: User = Depends(get_current_user_data),
#     db: Session = Depends(get_db)
# ):
#     user = db.query(User).filter(User.id == current_user.id).first()

#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")

#     db.delete(user)
#     db.commit()

#     return {"message": "Account and related data have been deleted successfully"}

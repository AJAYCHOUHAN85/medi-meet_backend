from pydantic import BaseModel, EmailStr
from typing import Optional , List

# ---------- User Schemas ----------
class UserBase(BaseModel):
    name: str
    email: EmailStr
    city: str
    phone_no :str

class UserCreate(UserBase):
    password: str



class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    city: str
    role: str

    class Config:
        orm_mode = True


# ============================= Reset password models ======================================



class RequestPasswordReset(BaseModel):
    email: EmailStr

class VerifyOTP(BaseModel):
    # email: EmailStr
    otp: str

class ResetPassword(BaseModel):
    email: EmailStr
    new_password: str



# ============================ User Update model ==============================================

class UserUpdate(BaseModel):
    name: Optional[str]  = None
    email: Optional[str] = None
    city : Optional[str] = None
    phone_no :Optional[str] = None 




# ---------- Doctor Schemas ----------


class DoctorCreate(BaseModel):
    specialization: str
    experience: int
    description: Optional[str] = None
    fees: Optional[int] = None
    certificate_pdf: Optional[str] = None

class DoctorResponse(BaseModel):
    id: int
    user_id: int
    specialization: str
    experience: int
    description: Optional[str]
    fees: Optional[int]
    certificate_pdf: Optional[str]

    class Config:
        orm_mode = True

class GetAllSlot(BaseModel):
    doctor_id :int 

class DocterApproved(BaseModel):
    approved :str

class GetSlotId(BaseModel):
    slot_id :int

class TimeRange(BaseModel):
    start : str
    end : str


class SlotCreateRequest(BaseModel):
    date :str
    availability : List[TimeRange]
    slot_duration : int


class DeleteSlot(BaseModel):
    id : int 


# ========================================== Category Schema =======================


class CreateCategory(BaseModel):
    category_name: str



class CategoryUpdate(BaseModel):
    category_name: Optional[str]  = None
    
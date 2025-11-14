from sqlalchemy import Column, Integer, String, Boolean, ForeignKey ,DateTime , DATE ,TIME
from database import Base
from datetime import datetime, timedelta

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    password = Column(String, nullable=False)
    city = Column(String, nullable=False)
    phone_no = Column(String)
    role = Column(String, default="user")
    status = Column(Boolean, default=True)



class PasswordResetToken(Base):
    __tablename__ = "password_reset_tokens"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    otp = Column(String)
    expires_at = Column(DateTime)
    is_used = Column(Boolean, default=False)


class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id" ,ondelete="CASCADE"), nullable=False)
    specialization = Column(String, nullable=False)
    experience = Column(Integer)
    description = Column(String)
    fees = Column(Integer)
    certificate_pdf = Column(String)
    status = Column(Boolean, default=True)
    approved = Column(Boolean , default = False)


class  DoctorSlot(Base):
    __tablename__ = "doctor_slot"
    id = Column(Integer ,primary_key=True , index=True)
    doctor_id = Column(Integer)
    date = Column(DATE , nullable=False)
    start_time =Column(TIME, nullable=False)
    end_time = Column(TIME, nullable=False)
    is_booked = Column(Boolean , default=False)




class Category(Base):
    __tablename__ = "category"
    id = Column(Integer,primary_key=True,index=True)
    category_name = Column(String)



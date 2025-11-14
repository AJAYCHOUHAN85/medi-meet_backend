from fastapi import FastAPI
from database import Base, engine
from routers import auth_router, doctor_router , user_profile ,setting_user_delete_acc ,setting_edit_profile , forget_password ,verify_otp ,reset_password ,create_slot , delete_slot , get_all_doctore_slot , book_slot
from routers.admin_routers import get_all_doctor, get_all_user
from routers.admin_routers import add_category , update_category ,get_all_category , delete_category , doctor_verification



Base.metadata.create_all(bind=engine)
app = FastAPI(title="MediMeet API")

app.include_router(auth_router.router)
app.include_router(doctor_router.router)
app.include_router(get_all_user.router)
app.include_router(get_all_doctor.router)
app.include_router(user_profile.router)
app.include_router(setting_user_delete_acc.router)
app.include_router(setting_edit_profile.router)
app.include_router(forget_password.router)
app.include_router(verify_otp.router)
app.include_router(reset_password.router)
app.include_router(add_category.router)
app.include_router(update_category.router)
app.include_router(get_all_category.router)
app.include_router(delete_category.router)
app.include_router(doctor_verification.router)
app.include_router(create_slot.router)
app.include_router(delete_slot.router)
app.include_router(get_all_doctore_slot.router)
app.include_router(book_slot.router)


@app.get("/")
def root():
    return {"message": "Welcome to MediMeet API"}

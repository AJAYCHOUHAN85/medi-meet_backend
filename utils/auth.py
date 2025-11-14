from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from fastapi import Header, HTTPException, status
from jose import jwt, JWTError
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session
from database import get_db
from models import User , Doctor
# OAuth2 config
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# Secret key setup
SECRET_KEY = "mysecretkey"  # ⚠️ Change this in production
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Password functions
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# Token functions
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)





breear_shemas = HTTPBearer()
def get_current_user(
    token: HTTPAuthorizationCredentials = Depends(breear_shemas),
    db: Session = Depends(get_db)
) -> int:
    """
    Extract user_id manually from the JWT token provided in the Authorization header.
    """
    if token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token header missing"
        )
    try:
        payload = jwt.decode(token.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = int(payload.get("sub"))
        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid token payload")
        return user_id
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    


breear_shemas = HTTPBearer()
def get_current_user_data(
    token: HTTPAuthorizationCredentials = Depends(breear_shemas),
    db: Session = Depends(get_db) ):
    
    if token is None :
     raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token header missing"
        ) 
    try:
        payload = jwt.decode(token.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        id : str = payload.get("sub")
        if id is None:
            raise HTTPException(status_code=401, detail="Invalid token payload")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token payload")
    
    user = db.query(User).filter(User.id == id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="data not found")
    return user




# ===============================================  is_admin dependency ========================================


def is_admin(
    current_user: User = Depends(get_current_user_data), 
    db: Session = Depends(get_db)
):
    # Fetch the user from DB to be sure
    user_in_db = db.query(User).filter(User.id == current_user.id).first()
    if not user_in_db:
        raise HTTPException(status_code=404, detail="User not found")
    if user_in_db.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to access this resource"
        )
    return user_in_db  # can return user info if needed






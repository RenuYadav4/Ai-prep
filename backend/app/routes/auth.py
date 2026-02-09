from fastapi import APIRouter, Depends  #type: ignore
from sqlalchemy.orm import Session  #type: ignore
from app.schemas.user import UserCreate, UserLogin, UserResponse
from app.dependencies.get_db import get_db
from app.services.user_service import register_user,login_user
from fastapi import status   #type: ignore


router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register",response_model=UserResponse,status_code=status.HTTP_201_CREATED)
def register(user: UserCreate,db: Session=Depends(get_db)):
    return register_user(db, user)

@router.post("/login")
def login(user: UserLogin,db: Session=Depends(get_db)):
    return login_user(db, user)

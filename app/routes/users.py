from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.core.security import create_access_token
from app.db.database import get_db
from app.schema import users as schemas
from app.services import users_service

router = APIRouter(tags=["Users"])




@router.post("/api/v1/auth/register")
def register_user(user: schemas.UserRegister, db: Session = Depends(get_db)):

    return users_service.register_user(db=db, email = user.email, password = user.password)



@router.post("/api/v1/auth/login")
def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    db_user = users_service.authenticate_user(
        db=db,
        email=form_data.username,
        password=form_data.password
    )

    access_token = create_access_token(
        data={"sub": str(db_user.id)}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


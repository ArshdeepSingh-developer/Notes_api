from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.core.exception import invalid_credential
from app.core.security import create_access_token, hash_password, verify_password
from app.db.database import SessionLocal, get_db
from app.schema import users as schemas
from app.db import models


router = APIRouter(tags=["Users"])




@router.post("/api/v1/auth/register")
def register_user(user: schemas.UserRegister, db: Session = Depends(get_db)):

    existing_user = db.query(models.User).filter(models.User.email == user.email).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pw = hash_password(user.password)

    new_user = models.User(
        email=user.email,
        password=hashed_pw
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User registered successfully"}



@router.post("/api/v1/auth/login")
def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    # form_data.username → email
    # form_data.password → password

    db_user = db.query(models.User).filter(
        models.User.email == form_data.username
    ).first()

    if not db_user:
        raise invalid_credential()

    if not verify_password(form_data.password, db_user.password):
        raise invalid_credential()

    access_token = create_access_token(
        data={"sub": str(db_user.id)}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.core.exception import invalid_credential
from app.core.security import hash_password, verify_password
from app.db import models


def register_user(db: Session, email: str, password: str):
    existing_user = db.query(models.User).filter(models.User.email == email).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pw = hash_password(password)

    new_user = models.User(
        email=email,
        password=hashed_pw
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User registered successfully"}

def authenticate_user(db: Session, email: str, password: str):
    db_user = db.query(models.User).filter(
        models.User.email == email
    ).first()

    if not db_user:
        raise invalid_credential()

    if not verify_password(password, db_user.password):
        raise invalid_credential()

    return db_user
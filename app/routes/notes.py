from fastapi import APIRouter, Depends, HTTPException, status
from typing import Optional
from sqlalchemy.orm import Session
from app.auth.auth import get_current_user
from app.core.exception import not_found_exception
from app.db.database import SessionLocal, get_db
from app.schema import note as schemas
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer
from app.core.config import SECRET_KEY, ALGORITHM
from app.db import models

router = APIRouter(prefix="/api/v1/notes", tags=["notes"])

oauth2_schema = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")




@router.post("/create", response_model=schemas.NoteResponse, status_code= status.HTTP_201_CREATED)
def create_note(
    note: schemas.NoteCreate,
    db: Session=Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    db_note = models.Note(title=note.title, content=note.content, owner_id=user_id)
    
    db.add(db_note)      # Add to session
    db.commit()          # Save to DB
    db.refresh(db_note)  # Get updated data (like ID)

    return db_note

@router.get("/", response_model=list[schemas.NoteResponse], status_code= status.HTTP_200_OK)
def search_notes(
    keyword: Optional[str] = None,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    query = db.query(models.Note).filter(
        models.Note.owner_id == user_id
    )

    if keyword:
        query = query.filter(
            models.Note.title.ilike(f"%{keyword}%")
        )

    return query.all()

@router.get("/{note_id}", response_model=schemas.NoteResponse, status_code=status.HTTP_200_OK)
def get_node_by_id(
    note_id: int, 
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
    ):
    note=db.query(models.Note).filter(models.Note.id == note_id, models.Note.owner_id == user_id).first()

    if not note:
        raise not_found_exception('note')
    
    return note


@router.put("/{note_id}", response_model=schemas.NoteResponse, status_code=status.HTTP_200_OK)
def update_note(
    note_id: int,
    updated_note: schemas.NoteUpdate,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):

    note = db.query(models.Note).filter(
        models.Note.id == note_id,
        models.Note.owner_id == user_id
    ).first()

    if not note:
        raise not_found_exception("note")

    note.title = updated_note.title
    note.content = updated_note.content

    db.commit()
    db.refresh(note)

    return note


@router.delete("/{note_id}", status_code=status.HTTP_200_OK)
def delete_note(
    note_id: int,  
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):

    note = db.query(models.Note).filter(
        models.Note.id == note_id,
        models.Note.owner_id == user_id
    ).first()

    if not note:
        raise not_found_exception('note')

    db.delete(note)
    db.commit()

    return {"message": "Note deleted successfully"}
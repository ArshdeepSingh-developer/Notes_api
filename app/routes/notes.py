from fastapi import APIRouter, Depends, HTTPException
from typing import Optional
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer
from app.config import SECRET_KEY, ALGORITHM

router = APIRouter(prefix="/api/v1/notes", tags=["notes"])

oauth2_schema = OAuth2PasswordBearer(tokenUrl="/login")

# Dependency to get DB session
def get_db():
    db =SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(token: str = Depends(oauth2_schema)):

    try:
        # Decode JWT token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        user_id: int = payload.get("user_id")

        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        return user_id

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")



@router.post("/create", response_model=schemas.NoteResponse)
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

@router.get("/",response_model=list[schemas.NoteResponse])
def get_notes(
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
    ):
    return db.query(models.Note).filter(models.Note.owner_id == user_id).all()
    
@router.get("/find/{note_id}", response_model=schemas.NoteResponse)
def get_node_by_id(
    note_id: int, 
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
    ):
    note=db.query(models.Note).filter(models.Note.id == note_id, models.Note.owner_id == user_id).first()

    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    
    return note

@router.get("/search", response_model=list[schemas.NoteResponse])
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


@router.put("/{note_id}", response_model=schemas.NoteResponse)
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
        raise HTTPException(status_code=404, detail="Note not found")

    note.title = updated_note.title
    note.content = updated_note.content

    db.commit()
    db.refresh(note)

    return note


@router.delete("/{note_id}")
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
        raise HTTPException(status_code=404, detail="Note not found")

    db.delete(note)
    db.commit()

    return {"message": "Note deleted successfully"}
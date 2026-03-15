from fastapi import APIRouter, Depends, HTTPException
from typing import Optional
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas

router = APIRouter(prefix="/api/v1/notes", tags=["notes"])

# Dependency to get DB session
def get_db():
    db =SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create", response_model=schemas.NoteResponse)
def create_note(
    note: schemas.NoteCreate,
    db: Session=Depends(get_db)
):
    db_note = models.Note(title=note.title, content=note.content)
    
    db.add(db_note)      # Add to session
    db.commit()          # Save to DB
    db.refresh(db_note)  # Get updated data (like ID)

    return db_note

@router.get("/",response_model=list[schemas.NoteResponse])
def get_notes(db: Session = Depends(get_db)):
    return db.query(models.Note).all()
    
@router.get("/find/{note_id}", response_model=schemas.NoteResponse)
def get_node_by_id(note_id: int, db: Session = Depends(get_db)):
    note=db.query(models.Note).filter(models.Note.id == note_id).first()

    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    
    return note

@router.get("/search", response_model=list[schemas.NoteResponse])
def search_notes(keyword: Optional[str] = None, db: Session = Depends(get_db)):
    if not keyword:
        return db.query(models.Note).all()
    result = db.query(models.Note).filter(models.Note.title.contains(keyword)).all()
    
    return result

@router.put("/update", response_model=schemas.NoteResponse)
def update_note(note_id: int, updated_note:schemas.NoteUpdate, db: Session = Depends(get_db)):
    note = db.query(models.Note).filter(models.Note.id == note_id).first()

    if not note:
        raise HTTPException(status_code=404, detail='note not found')
    note.title = updated_note.title
    note.content = updated_note.content

    db.commit()
    db.refresh(note)

    return note

@router.delete('/delete')
def delete_note(note_id: int, db: Session = Depends (get_db)):
    note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail='note not found')
    
    db.delete(note)
    db.commit()

    return {'message': 'note deleted successfully'}

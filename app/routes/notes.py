from fastapi import APIRouter, Depends, status
from typing import Optional
from sqlalchemy.orm import Session
from app.auth.auth import get_current_user
from app.db.database import get_db
from app.schema import note as schemas
from app.services.note_service import (
    create_note_service,
    get_user_notes_service,
    get_note_by_id_service,
    update_note_service,
    delete_note_service,
)

router = APIRouter(prefix="/api/v1/notes", tags=["notes"])


@router.post("/create", response_model=schemas.NoteResponse, status_code=status.HTTP_201_CREATED)
def create_note(
    note: schemas.NoteCreate,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    return create_note_service(db=db, user_id=user_id, title=note.title, content=note.content)


@router.get("/", response_model=list[schemas.NoteResponse], status_code=status.HTTP_200_OK)
def search_notes(
    keyword: Optional[str] = None,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    return get_user_notes_service(db=db, user_id=user_id, keyword=keyword)


@router.get("/{note_id}", response_model=schemas.NoteResponse, status_code=status.HTTP_200_OK)
def get_node_by_id(
    note_id: int,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    return get_note_by_id_service(db=db, user_id=user_id, note_id=note_id)


@router.put("/{note_id}", response_model=schemas.NoteResponse, status_code=status.HTTP_200_OK)
def update_note(
    note_id: int,
    updated_note: schemas.NoteUpdate,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    return update_note_service(db=db, user_id=user_id, note_id=note_id, title=updated_note.title, content=updated_note.content)


@router.delete("/{note_id}", status_code=status.HTTP_200_OK)
def delete_note(
    note_id: int,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    delete_note_service(db=db, user_id=user_id, note_id=note_id)

    return {"message": "Note deleted successfully"}
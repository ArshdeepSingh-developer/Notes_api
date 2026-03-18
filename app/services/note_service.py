from sqlalchemy.orm import Session
from app.db import models
from app.core.exception import not_found_exception


def create_note_service(db: Session, user_id: int, title: str, content: str):
    note = models.Note(
        title=title,
        content=content,
        owner_id=user_id
    )

    db.add(note)
    db.commit()
    db.refresh(note)

    return note


def get_user_notes_service(db: Session, user_id: int, keyword: str = None):
    query = db.query(models.Note).filter(
        models.Note.owner_id == user_id
    )

    if keyword:
        query = query.filter(
            models.Note.title.ilike(f"%{keyword}%")
        )

    return query.all()


def get_note_by_id_service(db: Session, user_id: int, note_id: int):
    note = db.query(models.Note).filter(
        models.Note.id == note_id,
        models.Note.owner_id == user_id
    ).first()

    if not note:
        raise not_found_exception('note')

    return note


def update_note_service(db: Session, user_id: int, note_id: int, title: str, content: str):
    note = get_note_by_id_service(db, user_id, note_id)

    note.title = title
    note.content = content

    db.commit()
    db.refresh(note)

    return note


def delete_note_service(db: Session, user_id: int, note_id: int):
    note = get_note_by_id_service(db, user_id, note_id)

    db.delete(note)
    db.commit()

    return True
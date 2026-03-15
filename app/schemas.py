# app/schemas.py

from pydantic import BaseModel


# Used when creating a note (request body)
class NoteCreate(BaseModel):
    title: str
    content: str


# Used when updating a note
class NoteUpdate(BaseModel):
    title: str
    content: str


# Used when returning a note (response model)
class NoteResponse(BaseModel):
    id: int
    title: str
    content: str

    # This allows returning SQLAlchemy objects directly
    class Config:
        from_attributes = True   # Use orm_mode = True if older Pydantic
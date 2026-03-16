from pydantic import BaseModel


class UserRegister(BaseModel):
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token : str
    token_type : str

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
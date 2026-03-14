from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Note(BaseModel):
    title:str
    content:str

notes_db = [
    {"id": 1, "title": "Learn FastAPI", "content": "FastAPI is fast"},
    {"id": 2, "title": "Learn Python", "content": "Python is powerful"},
    {"id": 3, "title": "GenAI", "content": "AI is the future"},
]


@app.get("/")
def read_root():
    return {"status": "Ok"}

@app.get("/notes")
def read_notes():
    return notes_db

@app.get("/notes/{notes_id}")
def get_note(notes_id: int):
    for note in notes_db:
        if note["id"] == notes_id:
            return note
    return {"error": "Note not found"}

@app.get("/search")
def search_notes(keyword:Optional[str] = None):
    if not keyword:
        return notes_db
    results = []
    for note in notes_db:
        if keyword.lower() in note["title"].lower():
            results.append(note)
    return results

@app.post("/notes")
def create_note(note: Note):
    new_note = {
        "id": len(notes_db) + 1,
        "title": note.title,
        "content": note.content
    }
    notes_db.append(new_note)
    return new_note

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    for note in notes_db:
        if(note['id'] ==note_id):
            notes_db.remove(note)
            return {"message":"Deleted"}
    return{"error": "not found"}

@app.put("/notes/{note_id}")
def update_note(note_id:int, updated_note:Note):
    for note in notes_db:
        if(note["id"] == note_id):
            note["title"] = updated_note.title
            note["content"] = updated_note.content
            return note
    return{"error": "not found"}
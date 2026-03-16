from fastapi import FastAPI
from app.database import engine
from app.models import Base
from app.routes import notes, users

app = FastAPI()

# Create tables in database automatically
Base.metadata.create_all(bind=engine)

# Include notes router
app.include_router(users.router)
app.include_router(notes.router)
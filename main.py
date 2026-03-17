from fastapi import FastAPI
from app.db.database import engine
from app.db.models import Base
from app.routes import notes, users
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables in database automatically
Base.metadata.create_all(bind=engine)

# Include notes router
app.include_router(users.router)
app.include_router(notes.router)
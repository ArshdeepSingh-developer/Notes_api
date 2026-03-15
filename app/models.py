# app/models.py

from sqlalchemy import Column, Integer, String
from .database import Base

# This class represents the "notes" table in the database
class Note(Base):
    __tablename__ = "notes"  # Table name in DB

    # Columns in table
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
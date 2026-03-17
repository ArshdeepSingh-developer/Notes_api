from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    notes = relationship("Note", back_populates="owner")


# This class represents the "notes" table in the database
class Note(Base):
    __tablename__ = "notes"  # Table name in DB

    # Columns in table
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner  = relationship("User", back_populates="notes")
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import DATABASE_URL



# Engine = connection to database
engine = create_engine(
    DATABASE_URL, 
    pool_size=5, 
    max_overflow=10
)

# SessionLocal = creates DB session instances
# A session is how we talk to the database
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Base class for all models (tables)
# Every model will inherit from this
Base = declarative_base()
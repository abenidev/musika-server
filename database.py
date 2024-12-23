from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from constants.key_constants import DATABASE_URL

# Database configuration
# sets up a connection to a PostgreSQL database and
# creates a session maker that can be used to create new database sessions.
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """
    Dependency that provides a database session.

    This function is used as a dependency in FastAPI to create a new
    SQLAlchemy database session. It yields a session and ensures that
    the session is closed after use, regardless of whether the operation
    was successful or not.

    Yields:
        Session: An instance of SQLAlchemy session.
    """

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

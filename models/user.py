from models.base import Base
from sqlalchemy import Column, TEXT, VARCHAR, LargeBinary

# LargeBinary, which means it can store binary data of arbitrary length (e.g., hashed passwords).


class User(Base):
    __tablename__ = 'users'
    id = Column(TEXT, primary_key=True)
    name = Column(VARCHAR(100))
    email = Column(VARCHAR(100))
    password = Column(LargeBinary)

    class Config:
        orm_mode = True

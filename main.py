from fastapi import FastAPI
from routes import auth
from models.base import Base
from database import engine

app = FastAPI()

# includes the auth router in the FastAPI app,
# prefixing all its routes with /auth and categorizing them under
# the auth tag in the API documentation.
app.include_router(auth.router, prefix='/auth', tags=['auth'])

# Create the users table
Base.metadata.create_all(engine)

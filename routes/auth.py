import uuid
import bcrypt
from database import get_db
from models.user import User
from pydantic_schemas.user_create import UserCreate
from fastapi import Depends, HTTPException, Header
from fastapi import APIRouter
from sqlalchemy.orm import Session
from constants.key_constants import JWTALGO, SECRETKEY
from middleware.auth_middleware import auth_middleware


from pydantic_schemas.user_login import UserLogin
import jwt


# Signup endpoint
router = APIRouter()


# defines a new endpoint for the API,
# specifically for signing up a user,
# that listens for HTTP POST requests to the "/signup" path and
# returns a status code of 201 (Created) by default.
@router.post("/signup", status_code=201)
def signup_user(user_create: UserCreate, db: Session = Depends(get_db)):
    """Create a new user.

    This endpoint creates a new user in the database. The user's email must be
    unique, and the password is hashed using bcrypt.

    Args:
        user_create (UserCreate): The user data to be created.

    Returns:
        User: The newly created user.

    Raises:
        HTTPException: 400 if the user already exists.
    """
    existing_user = db.query(User).filter(
        User.email == user_create.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    hashed_password = bcrypt.hashpw(
        user_create.password.encode("utf-8"), bcrypt.gensalt()
    )

    new_user = User(
        id=str(uuid.uuid4()),
        name=user_create.name,
        email=user_create.email,
        password=hashed_password,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.post('/login')
def login_user(credentials: UserLogin, db: Session = Depends(get_db)):
    """Login a user.

    This endpoint logs in a user and returns a JWT token to be used for
    authentication.

    Args:
        credentials (UserLogin): The user's email and password.

    Returns:
        dict: A dictionary containing the JWT token and the newly logged in user.

    Raises:
        HTTPException: 400 if the user is not found or if the password is incorrect.
    """
    user = db.query(User).filter(User.email == credentials.email).first()
    if not user:
        raise HTTPException(status_code=400, detail="User not found")

    is_password_match = bcrypt.checkpw(
        credentials.password.encode("utf-8"), user.password)

    if not is_password_match:
        raise HTTPException(status_code=400, detail="Incorrect password")

    token = jwt.encode({'id': user.id}, SECRETKEY, algorithm=JWTALGO)

    return {'token': token, 'user': user}


@router.get('/')
def get_current_user_data(db: Session = Depends(get_db), auth_data=Depends(auth_middleware)):
    """Get the current user's data.

    This endpoint returns the current user's data.

    Raises:
        HTTPException: 404 if the user is not found.
    """
    user = db.query(User).filter(User.id == auth_data['uid']).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user

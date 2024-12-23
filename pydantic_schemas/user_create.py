from pydantic import BaseModel

# Pydantic model for user creation

"""
defining a Pydantic model for user creation. 
It has three required fields: name, email, and password, 
all of which must be strings.
"""


class UserCreate(BaseModel):
    name: str
    email: str
    password: str

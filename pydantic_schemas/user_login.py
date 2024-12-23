from pydantic import BaseModel

"""
defines a Pydantic model named UserLogin 
with two fields: email and password, 
both of which are strings.
"""


class UserLogin(BaseModel):
    email: str
    password: str

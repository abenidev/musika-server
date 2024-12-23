from fastapi import HTTPException, Header
from constants.key_constants import SECRETKEY, JWTALGO

import jwt


def auth_middleware(x_auth_token=Header()):
    """
    Middleware to authenticate a user using a JWT token.

    Args:
        x_auth_token (str): The JWT token to authenticate with.

    Returns:
        dict: A dictionary containing the user id and the JWT token.

    Raises:
        HTTPException: If the token is invalid or missing.
    """
    try:
        if not x_auth_token:
            raise HTTPException(
                status_code=401, detail="Not authenticated: No token provided")

        verified_token = jwt.decode(
            x_auth_token, SECRETKEY, algorithms=[JWTALGO])
        if not verified_token:
            raise HTTPException(
                status_code=401, detail="Not authenticated: Token verification failed")
        uid = verified_token.get('id')
        return {'uid': uid, 'token': x_auth_token}
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=401, detail="Not authenticated: Invalid token")

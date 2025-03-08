"""Authentication models."""

# Authentication model

from dotenv import load_dotenv
from pydantic import BaseModel

from src.auth.utils import get_password_hash, verify_password

load_dotenv()

class Token(BaseModel):
    """Token value data."""

    access_token: str
    username: str

class TokenData(BaseModel):
    username: str | None = None



# def authenticate_user(fake_db, username: str, password: str):
#     #user = get_user(fake_db, username)
#     if not user:
#         return False
#     if not verify_password(password, user.hashed_password):
#         return False
#     return user

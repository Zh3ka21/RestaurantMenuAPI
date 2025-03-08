"""Authentication models."""

# Authentication model

from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()


class Token(BaseModel):
    """Token value data."""

    access_token: str
    username: str


class TokenData(BaseModel):
    username: str | None = None

"""Utils for auth."""

import os
from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from src.api.v1.employees.models import Employee
from src.database import get_db

SECRET_KEY = os.getenv("SECRET_KEY", "KEY")
ALGORITHM = os.getenv("ALGORITHM", "")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "1")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Initialize password context for hashing and verifying passwords
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """Hash function."""
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verification of plain and hashed password function."""
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> jwt:
    """Creation jwt token function."""
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=float(ACCESS_TOKEN_EXPIRE_MINUTES)))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> Employee:
    """Extract user from JWT token."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid authentication credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError as jwtErr:
        raise credentials_exception from jwtErr

    user = db.query(Employee).filter(Employee.name == username).first()
    if user is None:
        raise credentials_exception

    return user

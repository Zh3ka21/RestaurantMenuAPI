"""Routers for authentication."""

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from src.auth.utils import create_access_token, verify_password
from src.database import get_db
from src.employees.models import Employee

router = APIRouter()


@router.post("/login/")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
) -> dict:
    """Login into Employee account and return a JWT token."""
    db_employee = db.query(Employee).filter(Employee.name == form_data.username).first()

    if not db_employee or not verify_password(form_data.password, db_employee.password):  # type: ignore
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    # Generate JWT token
    token = create_access_token(data={"sub": db_employee.name})

    return {"access_token": token, "token_type": "bearer"}

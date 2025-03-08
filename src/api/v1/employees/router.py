"""Router for Employees."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session
from src.api.v1.auth.utils import hash_password
from src.api.v1.employees.models import Employee
from src.api.v1.employees.schemas import EmployeeCreate, EmployeeResponse
from src.database import get_db

router = APIRouter()


@router.post("/employees/", response_model=EmployeeResponse)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)) -> EmployeeResponse:
    """Create an employee function with enhanced error handling."""
    try:
        # Check if the employee already exists by name
        db_employee = db.query(Employee).filter(Employee.name == employee.name).first()

        if db_employee:
            raise HTTPException(status_code=400, detail="Employee already exists")

        # Create new employee
        hashed_password = hash_password(employee.password)
        new_employee = Employee(name=employee.name, password=hashed_password)

        db.add(new_employee)
        db.commit()
        db.refresh(new_employee)

        return EmployeeResponse(id=new_employee.id, name=new_employee.name)  # type: ignore

    except IntegrityError as ie:
        db.rollback()
        raise HTTPException(
            status_code=400, detail="Database integrity error: Possible duplicate entry",
        ) from ie

    except SQLAlchemyError as se:
        db.rollback()
        raise HTTPException(
            status_code=500, detail="Database error occurred",
        ) from se

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500, detail=f"Unexpected error: {e!s}",
        ) from e

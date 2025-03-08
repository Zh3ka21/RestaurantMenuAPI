"""Router for Employees."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from src.auth.utils import hash_password
from src.database import get_db
from src.employees.models import Employee
from src.employees.schemas import EmployeeCreate, EmployeeResponse

router = APIRouter()


@router.post("/employees/", response_model=EmployeeResponse)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)) -> EmployeeResponse:
    """Create an employee function."""
    # Check if the employee already exists by name
    db_employee = db.query(Employee).filter(Employee.name == employee.name).first()

    if db_employee:
        raise HTTPException(status_code=400, detail="Employee already exists")

    # Create new employee
    hashed_password = hash_password(employee.password)
    new_employee = Employee(name=employee.name, password=hashed_password)

    db.add(new_employee)
    try:
        db.commit()
        db.refresh(new_employee)
    except IntegrityError as ie:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error creating employee") from ie
    return EmployeeResponse(id=new_employee.id, name=new_employee.name)  # type: ignore

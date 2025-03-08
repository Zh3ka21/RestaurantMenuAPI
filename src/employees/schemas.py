"""Schema Employee."""

from pydantic import BaseModel


# Adding a Pydantic model for Employee
class EmployeeBase(BaseModel):
    name: str


class EmployeeCreate(EmployeeBase):
    password: str


class UserInDB(EmployeeCreate):
    password: str


class EmployeeResponse(EmployeeBase):
    id: int

    class Config:
        orm_mode = True

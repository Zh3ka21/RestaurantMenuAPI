"""Schema Employee."""

from pydantic import BaseModel


# Adding a Pydantic model for Employee
class EmployeeBase(BaseModel):
    name: str


class EmployeeCreate(EmployeeBase):
    hashed_password: str


class UserInDB(EmployeeCreate):
    hashed_password: str


class EmployeeResponse(EmployeeBase):
    id: int

    class Config:
        orm_mode = True

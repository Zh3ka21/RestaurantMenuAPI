"""Schema Employee."""

from pydantic import BaseModel


class EmployeeBase(BaseModel):
    """Base employee schema."""

    name: str


class EmployeeCreate(EmployeeBase):
    """Create employee schema."""

    password: str


class UserInDB(EmployeeCreate):
    """In db field employee schema."""

    password: str


class EmployeeResponse(EmployeeBase):
    """Employee response schema."""

    id: int

    class Config:
        """Class to configurate that orm should be used."""

        orm_mode = True

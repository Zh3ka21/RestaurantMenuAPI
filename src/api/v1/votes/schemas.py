"""Schema votes."""

from datetime import date

from pydantic import BaseModel


class VoteCreate(BaseModel):
    """Vote create schema."""

    employee_id: int
    date: date
    menu_id: int

    class Config:
        """Config to use orm."""

        orm_mode = True


class VoteResponse(BaseModel):
    """Vote Response schema."""

    id: int
    employee_id: int
    date: date
    menu_id: int

    class Config:
        """Config to use orm."""

        orm_mode = True

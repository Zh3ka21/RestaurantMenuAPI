"""Schema votes."""


from datetime import date

from pydantic import BaseModel


class VoteCreate(BaseModel):  # noqa: D101
    employee_id: int
    date: date
    menu_id: int

    class Config:  # noqa: D106
        orm_mode = True


class VoteResponse(BaseModel):  # noqa: D101
    id: int
    employee_id: int
    date: date
    menu_id: int

    class Config:  # noqa: D106
        orm_mode = True

"""Schema menus."""

from datetime import date

from pydantic import BaseModel


class MenuCreate(BaseModel):  # noqa: D101
    restaurant_id: int
    date: date | None
    items: str

    class Config:  # noqa: D106
        orm_mode = True

class MenuResponse(BaseModel):  # noqa: D101
    id: int
    restaurant_id: int
    date: date
    items: str

    class Config:  # noqa: D106
        orm_mode = True

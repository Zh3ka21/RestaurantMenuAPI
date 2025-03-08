"""Schema menus."""

from datetime import date

from pydantic import BaseModel


class MenuCreate(BaseModel):
    """Create Menu schema."""

    restaurant_id: int
    date: date | None
    items: str

    class Config:
        """Config to use orm."""

        orm_mode = True


class MenuResponse(BaseModel):
    """Create Menu schema."""

    id: int
    restaurant_id: int
    date: date
    items: str

    class Config:
        """Config to use orm."""

        orm_mode = True

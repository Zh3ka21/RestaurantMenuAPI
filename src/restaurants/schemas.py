"""Schema restaurants."""

from pydantic import BaseModel


class RestaurantCreate(BaseModel):  # noqa: D101
    name: str

class RestaurantResponse(RestaurantCreate):  # noqa: D101
    id: int

    class Config:  # noqa: D106
        orm_mode = True

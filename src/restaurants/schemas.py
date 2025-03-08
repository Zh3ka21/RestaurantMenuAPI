"""Schema restaurants."""

from pydantic import BaseModel


class RestaurantCreate(BaseModel):
    """Restaurant model schema."""

    name: str


class RestaurantResponse(RestaurantCreate):
    """Restaurant model Response schema."""

    id: int

    class Config:
        """Config to use orm."""

        orm_mode = True

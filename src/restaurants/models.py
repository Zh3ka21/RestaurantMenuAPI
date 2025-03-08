"""Restaurant model."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, validates

from src.database import Base


class Restaurant(Base):
    """Class Restaurant for representing restaurants."""

    __tablename__ = "restaurants"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    # Defining a relationship with the 'Menu' model
    menus = relationship("Menu", back_populates="restaurant")

    @validates("name")
    def validate_name(self, key: int, name: str) -> str:
        """Ensure restaurant name is not empty."""
        if not name:
            raise ValueError("Restaurant name cannot be empty")
        return name

"""Menu models."""

from datetime import date

from sqlalchemy import Column, Date, ForeignKey, ForeignKeyConstraint, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship, validates
from src.database import Base


class Menu(Base):
    """Class Menu for representing menus."""

    __tablename__ = "menus"
    id = Column(Integer, primary_key=True, index=True)
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"))
    date = Column(Date, default=date.today)
    items = Column(String)

    restaurant = relationship("Restaurant", back_populates="menus")

    __table_args__ = (
        UniqueConstraint("restaurant_id", "date", name="unique_menu"),
        ForeignKeyConstraint(
            ["restaurant_id"],
            ["restaurants.id"],
            ondelete="CASCADE",
        ),  # Ensure menu is linked to a valid restaurant
    )

    @validates("items")
    def validate_items(self, key: int, items: str) -> str:
        """Ensure menu has items."""
        if not items:
            raise ValueError("Menu items cannot be empty")
        return items

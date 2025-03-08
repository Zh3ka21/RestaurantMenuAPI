"""Vote model."""

from datetime import date

from sqlalchemy import Column, Date, ForeignKey, ForeignKeyConstraint, Integer, UniqueConstraint
from sqlalchemy.orm import validates

from src.database import Base


class Vote(Base):
    """Class Vote to represent votes of Employees."""

    __tablename__ = "votes"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    menu_id = Column(Integer, ForeignKey("menus.id"))
    date = Column(Date, default=date.today)

    __table_args__ = (
        UniqueConstraint("employee_id", "date", name="unique_vote"),
        ForeignKeyConstraint(["employee_id"], ["employees.id"], ondelete="CASCADE"),  # Ensure the employee exists
        ForeignKeyConstraint(["menu_id"], ["menus.id"], ondelete="CASCADE"),  # Ensure the menu exists
    )

    @validates("employee_id")
    def validate_employee(self, key: int, employee_id: int) -> int:
        """Ensure employee_id exists."""
        if not employee_id:
            raise ValueError("Employee ID cannot be empty")
        return employee_id

    @validates("menu_id")
    def validate_menu(self, key: int, menu_id: int) -> int:
        """Ensure menu_id exists."""
        if not menu_id:
            raise ValueError("Menu ID cannot be empty")
        return menu_id

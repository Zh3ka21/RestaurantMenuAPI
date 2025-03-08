"""Models.py for Employees."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
from src.database import Base


class Employee(Base):
    """Class Employee for company employees."""

    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    password = Column(String, nullable=False)

    @validates("name")
    def validate_name(self, key: int, name: str) -> str:
        """Ensure name is not empty."""
        if not name:
            raise ValueError("Employee name cannot be empty")
        return name

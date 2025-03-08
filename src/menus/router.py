"""Routers.py file."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.auth.utils import get_current_user
from src.database import get_db
from src.employees.models import Employee
from src.menus.schemas import MenuCreate, MenuResponse
from src.menus.services import create_menu, get_today_menu

router = APIRouter()


@router.post("/menus/", response_model=MenuResponse)
def create_menu_endpoint(
    menu: MenuCreate,
    db: Session = Depends(get_db),
) -> MenuResponse:
    """Menu create view."""
    db_menu = create_menu(menu, db)
    return MenuResponse.from_orm(db_menu)


# Get current day's menu
@router.get("/menu/today/", response_model=MenuResponse)
def get_today_menu_endpoint(
    db: Session = Depends(get_db), current_user: Employee = Depends(get_current_user)
) -> MenuResponse:
    """Menu for current day endpoint."""
    db_menu = get_today_menu(db)
    return MenuResponse.from_orm(db_menu)

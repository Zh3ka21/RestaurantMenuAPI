"""Services file."""

from datetime import date

from fastapi import HTTPException, status
from sqlalchemy import func
from sqlalchemy.orm import Session
from src.api.v1.menus.models import Menu
from src.api.v1.menus.schemas import MenuCreate
from src.api.v1.restaurants.models import Restaurant
from src.api.v1.votes.models import Vote


def create_menu(menu_data: MenuCreate, db: Session) -> Menu:
    """Create a menu function."""
    # Check if the restaurant with the given id exists
    restaurant = db.query(Restaurant).filter(Restaurant.id == menu_data.restaurant_id).first()
    if not restaurant:
        raise ValueError(f"Menu cannot exist without a valid restaurant with ID {menu_data.restaurant_id}")

    # Create a new Menu instance
    menu = Menu(
        restaurant_id=menu_data.restaurant_id,
        date=menu_data.date or date.today(),
        items=menu_data.items,
    )

    db.add(menu)
    db.commit()
    db.refresh(menu)
    return menu


def get_today_menu(db: Session) -> Menu:
    """Get today's menu based on the highest number of votes."""
    today = date.today()

    # Join Menu with Vote and count votes per menu
    menu = (
        db.query(Menu)
        .outerjoin(Vote, Menu.id == Vote.menu_id)
        .filter(Menu.date == today)
        .group_by(Menu.id)
        .order_by(func.count(Vote.id).desc())
        .first()
    )

    if not menu:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Menu for today not found.",
        )

    return menu

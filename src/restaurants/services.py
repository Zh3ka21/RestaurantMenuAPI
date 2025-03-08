"""Services file."""

from sqlalchemy.orm import Session

from src.restaurants.models import Restaurant
from src.restaurants.schemas import RestaurantCreate


def create_restaurant(restaurant_data: RestaurantCreate, db: Session) -> Restaurant:
    """Create a restaurant function."""
    restaurant = Restaurant(name=restaurant_data.name)
    db.add(restaurant)
    db.commit()
    db.refresh(restaurant)
    return restaurant

"""Routers.py file."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.restaurants.schemas import RestaurantCreate, RestaurantResponse
from src.restaurants.services import create_restaurant

router = APIRouter()


@router.post("/restaurants/", response_model=RestaurantResponse)
def create_restaurant_endpoint(
    restaurant: RestaurantCreate,
    db: Session = Depends(get_db),
) -> RestaurantResponse:
    """Restaurant create view."""
    return create_restaurant(restaurant, db)

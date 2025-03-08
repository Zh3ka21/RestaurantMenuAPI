"""Routers.py file."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.api.v1.restaurants.schemas import RestaurantCreate, RestaurantResponse
from src.api.v1.restaurants.services import create_restaurant
from src.database import get_db

router = APIRouter()


@router.post("/restaurants/", response_model=RestaurantResponse)
def create_restaurant_endpoint(
    restaurant: RestaurantCreate,
    db: Session = Depends(get_db),
) -> RestaurantResponse:
    """Restaurant create view."""
    return create_restaurant(restaurant, db)

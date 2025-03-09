"""Routers.py file."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import SQLAlchemyError
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
    try:
        return create_restaurant(restaurant, db)
    except HTTPException as http_exc:
        raise http_exc  # Re-raise known HTTP errors
    except SQLAlchemyError as se:
        raise HTTPException(
            status_code=500,
            detail="Database error occurred while creating restaurant",
        ) from se
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {e!s}") from e

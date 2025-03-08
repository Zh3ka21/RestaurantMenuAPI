"""Routers.py file."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session
from src.api.v1.auth.utils import get_current_user
from src.api.v1.employees.models import Employee
from src.api.v1.menus.schemas import MenuCreate, MenuResponse
from src.api.v1.menus.services import create_menu, get_today_menu
from src.database import get_db

router = APIRouter()


@router.post("/menus/", response_model=MenuResponse)
def create_menu_endpoint(
    menu: MenuCreate,
    db: Session = Depends(get_db),
) -> MenuResponse:
    """Menu create view with better error handling."""
    try:
        db_menu = create_menu(menu, db)
        return MenuResponse.from_orm(db_menu)
    except HTTPException as http_exc:
        raise http_exc  # Re-raise known HTTP errors
    except IntegrityError as ie:
        db.rollback()
        raise HTTPException(
            status_code=400, detail="Database integrity error: Possible duplicate entry"
        ) from ie
    except SQLAlchemyError as se:
        db.rollback()
        raise HTTPException(
            status_code=500, detail="Database error occurred while creating menu"
        ) from se
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500, detail=f"Unexpected error: {e!s}"
        ) from e


@router.get("/menu/today/", response_model=MenuResponse)
def get_today_menu_endpoint(
    db: Session = Depends(get_db),
    current_user: Employee = Depends(get_current_user),
) -> MenuResponse:
    """Menu for current day endpoint with improved error handling."""
    try:
        db_menu = get_today_menu(db)
        if not db_menu:
            raise HTTPException(status_code=404, detail="No menu found for today")
        return MenuResponse.from_orm(db_menu)
    except HTTPException as http_exc:
        raise http_exc  # Re-raise known HTTP errors
    except SQLAlchemyError as se:
        raise HTTPException(
            status_code=500, detail="Database error occurred while retrieving today's menu"
        ) from se
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Unexpected error: {e!s}"
        ) from e

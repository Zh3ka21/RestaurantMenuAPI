"""Routers.py file."""

from datetime import date

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session
from src.api.v1.auth.utils import get_current_user
from src.api.v1.employees.models import Employee
from src.api.v1.votes.models import Vote
from src.api.v1.votes.schemas import VoteCreate, VoteResponse
from src.api.v1.votes.services import create_vote
from src.database import get_db

router = APIRouter()


@router.post("/votes/", response_model=VoteResponse, status_code=status.HTTP_201_CREATED)
def create_vote_endpoint(
    vote_data: VoteCreate,
    db: Session = Depends(get_db),
    current_user: Employee = Depends(get_current_user),
) -> Vote:
    """Vote creating endpoint with enhanced error handling."""
    try:
        return create_vote(vote_data, db, current_user)
    except IntegrityError as ie:
        db.rollback()
        raise HTTPException(
            status_code=400, detail="Database integrity error: Possible duplicate vote entry"
        ) from ie
    except SQLAlchemyError as se:
        db.rollback()
        raise HTTPException(
            status_code=500, detail="Database error occurred while creating vote"
        ) from se
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500, detail=f"Unexpected error: {str(e)}"
        ) from e


@router.get("/votes/today/", response_model=list[VoteResponse])
def get_today_votes(
    db: Session = Depends(get_db), current_user: Employee = Depends(get_current_user)
) -> list[Vote]:
    """Retrieve current day's votes with error handling."""
    try:
        today = date.today()
        votes = db.query(Vote).filter(Vote.date == today).all()
        if not votes:
            raise HTTPException(status_code=404, detail="No votes found for today")
        return votes
    except SQLAlchemyError as se:
        raise HTTPException(
            status_code=500, detail="Database error occurred while retrieving today's votes"
        ) from se
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Unexpected error: {str(e)}"
        ) from e

"""Routers.py file."""

from datetime import date

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.auth.utils import get_current_user
from src.database import get_db
from src.employees.models import Employee
from src.votes.models import Vote
from src.votes.schemas import VoteCreate, VoteResponse
from src.votes.services import create_vote

router = APIRouter()


@router.post("/votes/", response_model=VoteResponse, status_code=status.HTTP_201_CREATED)
def create_vote_endpoint(
    vote_data: VoteCreate,
    db: Session = Depends(get_db),
    current_user: Employee = Depends(get_current_user),
) -> Vote:
    """Vote creating endpoint."""
    return create_vote(vote_data, db, current_user)


# Get current day votes
@router.get("/votes/today/", response_model=list[VoteResponse])
def get_today_votes(db: Session = Depends(get_db), current_user: Employee = Depends(get_current_user)) -> list[Vote]:
    """Retrieve current votes."""
    today = date.today()
    return db.query(Vote).filter(Vote.date == today).all()

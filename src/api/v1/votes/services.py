"""Services for vote class."""

from datetime import date

from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from src.api.v1.employees.models import Employee
from src.api.v1.votes.models import Vote
from src.api.v1.votes.schemas import VoteCreate


def create_vote(vote_data: VoteCreate, db: Session, current_user: Employee) -> Vote:
    """Create a vote."""
    today = date.today()
    existing_vote = (
        db.query(Vote)
        .filter(
            Vote.employee_id == current_user.id,
            Vote.date == today,
        )
        .first()
    )

    if existing_vote:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="You have already voted today.",
        )

    # Create the new vote
    vote = Vote(
        employee_id=current_user.id,
        date=today,
        menu_id=vote_data.menu_id,
    )

    db.add(vote)
    db.commit()
    db.refresh(vote)

    return vote

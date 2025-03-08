"""Main application py file."""

# FastAPI app
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer

from src.auth.router import router as auth_router
from src.database import create_tables
from src.employees.router import router as employee_router
from src.menus.router import router as menu_router
from src.restaurants.router import router as restaurant_router
from src.votes.router import router as vote_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Create database tables."""
    create_tables()
    yield


# Pass the lifespan handler to the FastAPI app
app = FastAPI(lifespan=lifespan)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app.include_router(restaurant_router)
app.include_router(menu_router)
app.include_router(vote_router)
app.include_router(employee_router)
app.include_router(auth_router)


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

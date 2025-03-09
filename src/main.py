"""Main application py file."""

# FastAPI app
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer

from src.api.v1.auth.router import router as auth_router
from src.api.v1.employees.router import router as employee_router
from src.api.v1.menus.router import router as menu_router
from src.api.v1.restaurants.router import router as restaurant_router
from src.api.v1.votes.router import router as vote_router
from src.database import create_tables


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

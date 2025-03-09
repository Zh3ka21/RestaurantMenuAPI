# Restaurant Voting API

A backend service that helps employees make decisions about lunch places. This API allows restaurants to upload daily menus and employees to vote for their preferred lunch options.

## Project Overview

This system provides an internal service for company employees to vote on daily restaurant menus for lunch decisions. Key features include:

- Restaurant management and menu uploads
- Employee registration and authentication
- Daily menu retrieval
- Vote submission and results viewing
- Versioning support for different mobile app builds

## Tech Stack

- **FastAPI**: Modern, high-performance web framework
- **JWT**: JSON Web Token authentication
- **PostgreSQL**: Relational database
- **Docker**: Containerization with docker-compose
- **PyTest**: Testing framework

## Setup Instructions

### Prerequisites

- Docker and Docker Compose
- Python 3.10+

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Zh3ka21/RestaurantMenuAPI.git
   cd RestaurantMenuAPI
   ```

2. Create a `.env` file in the project root with the following variables(example.env):

   ```
    POSTGRES_DB=""
    POSTGRES_USER=""
    POSTGRES_PASSWORD=""
    PORT=""
   ```

3. Build and start the containers:

   ```bash
   docker-compose up -d
   ```

4. The API should now be running at `http://localhost:8000`.

## API Documentation

After starting the service, visit `http://localhost:8000/docs` for the interactive Swagger UI documentation.

### Authentication

Endpoints (GetTodayMenu, CreateVote, VotesToday) require authentication via JWT token.

Authentication header format:

```
Authorization: Bearer {token}
```

### Endpoints

#### Authentication

- **POST /login/**
  Authenticates a user and returns a JWT token.

#### Restaurants

- **POST /restaurants/**
  Create a new restaurant.

#### Menus

- **POST /menus/**
  Upload a menu for a restaurant for a specific day.
- **GET /menu/today/**
  Get menus available for the current day.

#### Votes

- **POST /votes/**
  Submit a vote for a menu.
- **GET /votes/today/**
  Get voting results for the current day.

#### Employees

- **POST /employees/**
  Register a new employee in the system.

#### Root

- **GET /**
  Health check endpoint.

## Data Models

### Restaurant

```json
{
  "id": "id",
  "name": "string"
}
```

### Menu

```json
{
  "id": "id",
  "restaurant_id": "id",
  "date": "date",
  "items": "string"
}
```

### Employee

```json
{
  "id": "id",
  "username": "string",
  "password": "string"
}
```

### Vote

```json
{
  "id": "id",
  "employee_id": "id",
  "menu_id": "id",
  "date": "date"
}
```

## Project Structure

```
.
├── docker-compose.yaml
├── Dockerfile
├── example.env
├── poetry.lock
├── poetry.toml
├── pyproject.toml
├── README.md
├── requirements.txt
├── src
│   ├── api
│   │   └── v1
│   │       ├── auth
│   │       │   ├── __init__.py
│   │       │   ├── router.py
│   │       │   └── utils.py
│   │       ├── employees
│   │       │   ├── __init__.py
│   │       │   ├── models.py
│   │       │   ├── router.py
│   │       │   └── schemas.py
│   │       ├── menus
│   │       │   ├── __init__.py
│   │       │   ├── models.py
│   │       │   ├── router.py
│   │       │   ├── schemas.py
│   │       │   └── services.py
│   │       ├── restaurants
│   │       │   ├── __init__.py
│   │       │   ├── models.py
│   │       │   ├── router.py
│   │       │   ├── schemas.py
│   │       │   └── services.py
│   │       └── votes
│   │           ├── __init__.py
│   │           ├── models.py
│   │           ├── router.py
│   │           ├── schemas.py
│   │           └── services.py
│   ├── config.py
│   ├── database.py
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   └── utils.py
├── start_server.sh
└── tests
    ├── __init__.py
    └── test_auth.py
```

# Environment Setup

If you're using Poetry for dependency management:
Install dependencies

```
  poetry install
```

# Activate the virtual environment

```
  poetry shell
```

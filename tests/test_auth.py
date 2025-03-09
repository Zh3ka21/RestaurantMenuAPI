import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.api.v1.auth.utils import hash_password
from src.api.v1.employees.models import Employee
from src.database import Base

# Set up an in-memory SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    """Ensure the test database is initialized before running tests."""
    # Create all tables in the test database
    Base.metadata.create_all(bind=engine)
    yield  # Tests will run after this
    # Optional cleanup: Drop all tables after tests run
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def db_session():
    """Create a new database session for each test."""
    db = SessionLocal()
    yield db
    db.close()


@pytest.fixture(scope="function")
def test_employee(db_session):
    """Create a test employee in the test database with unique data."""
    new_employee = Employee(name="test_user_1", password=hash_password("123456789"))
    db_session.add(new_employee)
    db_session.commit()
    db_session.refresh(new_employee)
    return new_employee


def test_create_employee(db_session, test_employee):
    """Test if the employee is correctly created in the database."""
    # Query the employee from the database
    employee = db_session.query(Employee).filter(Employee.name == "test_user_1").first()
    assert employee is not None
    assert employee.name == "test_user_1"


def test_update_employee(db_session):
    """Test if an employee's information can be updated correctly."""
    # Create a new employee for this test
    employee = Employee(name="test_user_2", password=hash_password("123456789"))
    db_session.add(employee)
    db_session.commit()

    # Update the employee's name
    employee.name = "updated_user_2"
    db_session.commit()

    # Query the updated employee
    updated_employee = db_session.query(Employee).filter(Employee.name == "updated_user_2").first()
    assert updated_employee is not None
    assert updated_employee.name == "updated_user_2"


def test_delete_employee(db_session):
    """Test if an employee can be deleted from the database."""
    # Create a new employee for this test
    employee = Employee(name="test_user_3", password=hash_password("123456789"))
    db_session.add(employee)
    db_session.commit()

    # Delete the employee
    db_session.delete(employee)
    db_session.commit()

    # Query for the deleted employee
    deleted_employee = db_session.query(Employee).filter(Employee.name == "test_user_3").first()
    assert deleted_employee is None


def test_employee_password_hashing(db_session):
    """Test if the password is hashed correctly."""
    employee = Employee(name="hashed_user_1", password=hash_password("newpassword"))
    db_session.add(employee)
    db_session.commit()
    db_session.refresh(employee)

    # Check if the password is hashed
    assert employee.password != "newpassword"  # The password should not be in plain text
    assert len(employee.password) > 0  # The password should have a non-zero length

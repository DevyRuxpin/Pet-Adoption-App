import os
import pytest
from app import app as flask_app
from models import db, Pet

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # ensure the app is configured for testing
    flask_app.config.from_object('config.TestConfig')
    
    # Create the database and tables
    with flask_app.app_context():
        db.create_all()
    
    yield flask_app
    
    # Clean up / reset resources
    with flask_app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

@pytest.fixture
def session(app):
    """A database session for the tests."""
    with app.app_context():
        yield db.session

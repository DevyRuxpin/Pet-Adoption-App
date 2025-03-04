import pytest
from app import app as flask_app
from models import db

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    flask_app.config['TESTING'] = True
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/adopt_test'
    flask_app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF for testing
    
    # Create tables for each test
    with flask_app.app_context():
        db.create_all()
    
    yield flask_app
    
    # Clean up after each test
    with flask_app.app_context():
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

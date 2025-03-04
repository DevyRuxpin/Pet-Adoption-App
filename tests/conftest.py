import pytest
from app import app as flask_app
from models import db, Pet
from forms import AddPetForm, EditPetForm

@pytest.fixture
def app():
    flask_app.config['TESTING'] = True
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/adopt_test'
    flask_app.config['WTF_CSRF_ENABLED'] = False
    
    with flask_app.app_context():
        db.create_all()
        yield flask_app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def sample_pet():
    pet = Pet(
        name="TestPet",
        species="dog",
        photo_url="http://example.com/photo.jpg",
        age=5,
        notes="Test notes",
        available=True
    )
    db.session.add(pet)
    db.session.commit()
    return pet

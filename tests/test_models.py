import pytest
from models import Pet, db

def test_pet_model(app):
    """Test basic pet model"""
    with app.app_context():
        # Clear any existing data
        db.drop_all()
        db.create_all()
        
        pet = Pet(
            name="TestPet",
            species="dog",
            photo_url="http://example.com/photo.jpg",
            age=3,
            notes="Test notes",
            available=True
        )
        
        db.session.add(pet)
        db.session.commit()

        assert pet.id is not None
        assert pet.name == "TestPet"
        assert pet.species == "dog"
        assert pet.available is True

        # Clean up
        db.session.remove()
        db.drop_all()

def test_image_url(app):
    """Test image_url method"""
    with app.app_context():
        # Clear any existing data
        db.drop_all()
        db.create_all()
        
        # Test with photo_url
        pet1 = Pet(
            name="TestPet1",
            species="cat",
            photo_url="http://example.com/photo.jpg"
        )
        assert pet1.image_url() == "http://example.com/photo.jpg"

        # Test without photo_url
        pet2 = Pet(
            name="TestPet2",
            species="dog"
        )
        assert "default" in pet2.image_url().lower()

        # Clean up
        db.session.remove()
        db.drop_all()

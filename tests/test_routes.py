import pytest
from models import Pet, db

def test_homepage(client):
    """Test homepage route"""
    resp = client.get('/')
    assert resp.status_code == 200
    assert b'Our Pets' in resp.data

def test_add_pet(app, client):
    """Test add pet route"""
    with app.app_context():
        db.drop_all()
        db.create_all()
        
        data = {
            'name': 'TestPet',
            'species': 'dog',
            'photo_url': 'http://example.com/photo.jpg',
            'age': '3',
            'notes': 'Test notes about this pet'
        }
        
        resp = client.post('/add', data=data, follow_redirects=True)
        assert resp.status_code == 200
        
        pet = Pet.query.filter_by(name='TestPet').first()
        assert pet is not None
        assert pet.species == 'dog'

        # Clean up
        db.session.remove()
        db.drop_all()

def test_edit_pet(app, client):
    """Test edit pet route"""
    with app.app_context():
        db.drop_all()
        db.create_all()
        
        # Create a pet
        pet = Pet(
            name="TestPet",
            species="dog",
            photo_url="http://example.com/photo.jpg",
            age=3,
            notes="Original notes",
            available=True
        )
        db.session.add(pet)
        db.session.commit()
        pet_id = pet.id

        # Test GET request
        resp = client.get(f'/{pet_id}')
        assert resp.status_code == 200
        assert b'TestPet' in resp.data

        # Test POST request
        data = {
            'photo_url': 'http://example.com/new-photo.jpg',
            'notes': 'Updated notes about this pet',
            'available': 'false'
        }
        
        resp = client.post(f'/{pet_id}', data=data, follow_redirects=True)
        assert resp.status_code == 200

        updated_pet = Pet.query.get(pet_id)
        assert updated_pet.photo_url == 'http://example.com/new-photo.jpg'
        assert updated_pet.notes == 'Updated notes about this pet'
        assert updated_pet.available is False

        # Clean up
        db.session.remove()
        db.drop_all()

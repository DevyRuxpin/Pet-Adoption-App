import pytest
from forms import AddPetForm, EditPetForm

def test_add_pet_form_validation(app):
    """Test AddPetForm validation"""
    with app.app_context():
        with app.test_request_context():
            form = AddPetForm()
            
            # Test empty form
            assert not form.validate()
            
            # Test valid data
            form = AddPetForm(data={
                'name': 'Fluffy',
                'species': 'cat',
                'photo_url': 'http://example.com/photo.jpg',
                'age': 2,
                'notes': 'A very good cat'
            })
            assert form.validate()

def test_edit_pet_form_validation(app):
    """Test EditPetForm validation"""
    with app.app_context():
        with app.test_request_context():
            form = EditPetForm()
            
            # Empty form should be valid since all fields are optional
            assert form.validate()
            
            # Test with data
            form = EditPetForm(data={
                'photo_url': 'http://example.com/photo.jpg',
                'notes': 'Updated notes about the pet',
                'available': True
            })
            assert form.validate()


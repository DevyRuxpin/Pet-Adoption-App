import pytest
from forms import AddPetForm, EditPetForm

def test_add_pet_form_validation(app):
    """Test AddPetForm validation"""
    with app.app_context():
        with app.test_request_context():
            # Test valid data
            form = AddPetForm(data={
                'name': 'Fluffy',
                'species': 'cat',
                'photo_url': 'http://example.com/photo.jpg',
                'age': 2,
                'notes': 'A very good cat'
            })
            # WTF_CSRF_ENABLED is False in test config, so this should work
            assert form.validate() == True, f"Form validation failed: {form.errors}"

            # Test empty form
            empty_form = AddPetForm(data={})
            assert empty_form.validate() == False

def test_edit_pet_form_validation(app):
    """Test EditPetForm validation"""
    with app.app_context():
        with app.test_request_context():
            # Test with valid data
            form = EditPetForm(data={
                'photo_url': 'http://example.com/photo.jpg',
                'notes': 'Updated notes about the pet',
                'available': True
            })
            assert form.validate() == True, f"Form validation failed: {form.errors}"

            # Empty form should be valid since all fields are optional
            empty_form = EditPetForm(data={})
            assert empty_form.validate() == True

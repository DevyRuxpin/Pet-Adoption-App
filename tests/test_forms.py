import pytest
from forms import AddPetForm, EditPetForm

def test_add_pet_form_validation(app):
    """Test AddPetForm validation"""
    with app.app_context():
        with app.test_request_context():
            # Create form with data
            form_data = {
                'name': 'Fluffy',  # required
                'species': 'cat',  # required, must be one of the choices
                'photo_url': 'http://example.com/photo.jpg',  # optional
                'age': 2,  # optional
                'notes': 'A very good cat'  # optional
            }
            
            form = AddPetForm(formdata=None)
            form.process(formdata=None, data=form_data)
            
            valid = form.validate()
            if not valid:
                print("Validation errors:", form.errors)  # Debug print
            assert valid, f"Form validation failed: {form.errors}"

            # Test empty form
            empty_form = AddPetForm(formdata=None)
            assert not empty_form.validate(), "Empty form should not validate"

def test_edit_pet_form_validation(app):
    """Test EditPetForm validation"""
    with app.app_context():
        with app.test_request_context():
            # Test with valid data
            form_data = {
                'photo_url': 'http://example.com/photo.jpg',
                'notes': 'Updated notes about this pet',
                'available': True
            }
            
            form = EditPetForm(formdata=None)
            form.process(formdata=None, data=form_data)
            assert form.validate(), f"Form validation failed: {form.errors}"

            # Empty form should be valid since all fields are optional
            empty_form = EditPetForm(formdata=None)
            assert empty_form.validate(), "Empty edit form should validate"

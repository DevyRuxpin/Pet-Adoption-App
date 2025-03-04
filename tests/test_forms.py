import pytest
from forms import AddPetForm, EditPetForm
from flask import request

def test_add_pet_form_validation(app):
    """Test AddPetForm validation"""
    with app.app_context():
        with app.test_request_context(method='POST', data={
            'name': 'Fluffy',
            'species': 'cat',
            'photo_url': 'http://example.com/photo.jpg',
            'age': '2',
            'notes': 'A very good cat'
        }):
            form = AddPetForm()
            assert form.validate(), f"Form validation failed: {form.errors}"

        # Test empty form
        with app.test_request_context(method='POST', data={}):
            empty_form = AddPetForm()
            assert not empty_form.validate(), "Empty form should not validate"

def test_edit_pet_form_validation(app):
    """Test EditPetForm validation"""
    with app.app_context():
        with app.test_request_context(method='POST', data={
            'photo_url': 'http://example.com/photo.jpg',
            'notes': 'Updated notes about this pet',
            'available': 'true'
        }):
            form = EditPetForm()
            assert form.validate(), f"Form validation failed: {form.errors}"

        # Empty form should be valid since all fields are optional
        with app.test_request_context(method='POST', data={}):
            empty_form = EditPetForm()
            assert empty_form.validate(), "Empty edit form should validate"


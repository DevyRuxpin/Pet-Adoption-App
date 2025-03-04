"""Tests for forms."""

from forms import AddPetForm, EditPetForm

def test_add_pet_form_validation(app):
    """Test add pet form validation."""
    form = AddPetForm(
        name="TestPet",
        species="dog",
        photo_url="http://example.com/photo.jpg",
        age="5",
        notes="Test notes"
    )
    assert form.validate() == True

    # Test invalid species
    form = AddPetForm(
        name="TestPet",
        species="elephant",  # not in choices
        photo_url="http://example.com/photo.jpg"
    )
    assert form.validate() == False

def test_edit_pet_form_validation(app):
    """Test edit pet form validation."""
    form = EditPetForm(
        photo_url="http://example.com/photo.jpg",
        notes="Updated test notes",
        available=False
    )
    assert form.validate() == True

    # Test invalid URL
    form = EditPetForm(
        photo_url="not-a-url",
        notes="Updated test notes"
    )
    assert form.validate() == False

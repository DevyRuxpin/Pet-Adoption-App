"""Tests for Pet model."""

def test_pet_model(app, sample_pet):
    """Test basic model."""
    assert sample_pet.name == "TestPet"
    assert sample_pet.species == "dog"
    assert sample_pet.available == True

def test_image_url(app, sample_pet):
    """Test image_url method."""
    assert sample_pet.image_url() == "http://example.com/photo.jpg"
    
    # Test default image
    sample_pet.photo_url = None
    assert "nophoto.gif" in sample_pet.image_url()

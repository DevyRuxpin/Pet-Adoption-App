"""Tests for views."""

def test_homepage(client):
    """Test homepage."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Our Pets' in response.data

def test_add_pet(client):
    """Test add pet route."""
    # Test GET request
    response = client.get('/add')
    assert response.status_code == 200
    assert b'Add a Pet' in response.data

    # Test POST request
    data = {
        'name': 'NewPet',
        'species': 'cat',
        'photo_url': 'http://example.com/photo.jpg',
        'age': '3',
        'notes': 'Test notes for new pet'
    }
    response = client.post('/add', data=data, follow_redirects=True)
    assert response.status_code == 200
    assert b'NewPet' in response.data

def test_edit_pet(client, sample_pet):
    """Test edit pet route."""
    # Test GET request
    response = client.get(f'/{sample_pet.id}')
    assert response.status_code == 200
    assert sample_pet.name.encode() in response.data

    # Test POST request
    data = {
        'photo_url': 'http://example.com/new-photo.jpg',
        'notes': 'Updated test notes',
        'available': False
    }
    response = client.post(f'/{sample_pet.id}', data=data, follow_redirects=True)
    assert response.status_code == 200
    assert b'Updated test notes' in response.data

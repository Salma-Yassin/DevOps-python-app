import pytest
from add_numbers import app



@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_add_numbers(client):
    # Test with num1=5 and num2=10
    response = client.get('/add?num1=5&num2=10')
    assert response.status_code == 200
    assert response.data == b'15'

    # Test with num1=-3 and num2=8
    response = client.get('/add?num1=-3&num2=8')
    assert response.status_code == 200
    assert response.data == b'5'

    # Test with num1=0 and num2=0
    response = client.get('/add?num1=0&num2=0')
    assert response.status_code == 200
    assert response.data == b'0'

    # Test with missing num1 parameter
    response = client.get('/add?num2=10')
    assert response.status_code == 400
    assert response.data == b'Error: missing argument(s)'

    # Test with missing num2 parameter
    response = client.get('/add?num1=5')
    assert response.status_code == 400
    assert response.data == b'Error: missing argument(s)'

    # Test with non-integer num1 parameter
    response = client.get('/add?num1=foo&num2=10')
    assert response.status_code == 400
    assert response.data == b'Error: invalid argument(s)'

    # Test with non-integer num2 parameter
    response = client.get('/add?num1=5&num2=bar')
    assert response.status_code == 400
    assert response.data == b'Error: invalid argument(s)'
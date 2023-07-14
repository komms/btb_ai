from pathlib import Path
import pytest
import requests_mock
import sys


# Add the project root directory to the Python path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from btb_ai import app

@pytest.fixture
def client():
    app.testing = True
    client = app.test_client()
    return client


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello' in response.data


def test_process_image(client):
        with requests_mock.Mocker() as mocker:
            # Mock the requests.post method and define the expected response
            expected_response = {
                 "tags": "book, bookcase, bookshelf, fill, shelf, shelve"
                 }
            mocker.post('http://localhost:5000/process_image', json=expected_response)

            # Send a POST request to the '/process-image' endpoint
            data = {'image_path': 'imgs/photo_5440411542173633301_y.jpg'}
            response = client.post('/process_image', json=data)

            # Assert the response status code and content
            assert response.status_code == 200
            assert response.json == expected_response
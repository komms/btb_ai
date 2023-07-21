import json
import pytest
import requests_mock
import sys

from pathlib import Path

# Add the project root directory to the Python path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from btb_ai import app
from btb_ai.views.ai_model import image_to_data_uri


@pytest.fixture
def client():
    app.testing = True
    client = app.test_client()
    return client


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello" in response.data


def test_process_image(client):
    with requests_mock.Mocker() as mocker:
        # Mock the requests.post method and define the expected response
        expected_response = {"tags": "book, bookcase, bookshelf, fill, shelf, shelve"}
        mocker.post("http://localhost:5000/process_image", json=expected_response)

        # Send a POST request to the '/process-image' endpoint
        data = {"image_path": "imgs/photo_5440411542173633301_y.jpg"}
        response = client.post("/process_image", json=data)

        # Assert the response status code and content
        assert response.status_code == 200
        assert response.json == expected_response


def test_scene_explain(client):
    with requests_mock.Mocker() as mocker:
        # Mock the requests.post method and define the expected response
        with open("data/scene_explain_describe.json") as f:
            response = json.load(f)
        expected_response = {
            "classification": response["results"][0]["i18n"]["en"],
            "description": response["results"][0]["output"],
        }
        mocker.post("http://localhost:5000/scene_explain", json=expected_response)

        # Send a POST request to the '/scene_explain' endpoint
        img_path = "data/imgs/photo-1511108690759-009324a90311.jpeg"
        data = {
            "data": [
                {
                    "image": image_to_data_uri(img_path),
                    "features": ["question_answer"],
                    "style": "concise",
                    "question": "What is the thing in one word",
                },
            ]
        }
        response = client.post("/scene_explain", json=data)

        # Assert the response status code and content
        assert response.status_code == 200
        assert response.json == expected_response

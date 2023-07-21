"""
Script contains AI models API that understand and describe the scene
"""
import base64
import json
import os
import requests

from dotenv import load_dotenv
from flask import jsonify, abort, request

import replicate
from jinaai import JinaAI

from btb_ai import app


# Load variables from .env file
load_dotenv()
# Access environment variables
scene_explain_token = os.environ.get("SCENE_EXPLAIN_TOKEN")


jinaai = JinaAI(
    secrets={
        "scenex-secret": scene_explain_token,
        "promptperfect-secret": "XXXXXX",
        "rationale-secret": "XXXXXX",
        "jinachat-secret": "XXXXXX",
    }
)


"""
@app.before_request
def send_image_to_process():
    "Imitation of a middleware"
    if request.path == '/process_image':
        # Assuming the image file is located on the server
        data = {'image_path':'data/ imgs/photo_5440411542173633301_y.jpg'}
        response = requests.post('http://localhost:5000/process_image', data=data) """


def image_to_data_uri(file_path):
    with open(file_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode("utf-8")
        return f"data:image/jpeg;base64,{encoded_image}"


def toBase64(img: str) -> str:
    return jinaai.utils.image_to_base64(f"{img}")


@app.route("/process_image", methods=["POST", "GET"])
def process_image():
    """
    Recognise Anything with Segment Anything using Replicate API
    https://github.com/xinyu1205/recognize-anything/tree/main
    https://github.com/IDEA-Research/Grounded-Segment-Anything
    """
    # TODO: img_path as request data
    # uncomment use the API, limited credits so using the dummy_response.json for now.
    """     image_path = 'data/imgs/photo_5440411542173633301_y.jpg'
    output = replicate.run(
            "idea-research/ram-grounded-sam:80a2aede4cf8e3c9f26e96c308d45b23c350dd36f1c381de790715007f1ac0ad",
            input={"input_image": open(image_path, "rb")}
        ) """
    with open("data/GSAM_response.json") as f:
        output = json.load(f)
    return jsonify({"tags": output["tags"]})


@app.route("/scene_explain", methods=["GET", "POST"])
def scene_explain():
    """
    https://scenex.jina.ai/
    https://github.com/jina-ai/jinaai-py/
    """
    # uncomment to use API
    #     img_path = 'data/imgs/photo-1511108690759-009324a90311.jpeg'
    #     data = {
    #     "data": [
    #         {"image": image_to_data_uri(img_path), "features": ["question_answer"], "style": "concise", "question": "What is the thing in one word"},
    #     ]
    # }
    #     response = jinaai.describe(data)
    with open("data/scene_explain_describe.json") as f:
        response = json.load(f)
    return jsonify(
        {
            "classification": response["results"][0]["i18n"]["en"],
            "description": response["results"][0]["output"],
        }
    )


@app.route("/")
def index():
    return "Hello"
    # abort(404)

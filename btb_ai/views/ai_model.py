"""
Recognise Anything with Segment Anything using Replicate API
https://github.com/xinyu1205/recognize-anything/tree/main
https://github.com/IDEA-Research/Grounded-Segment-Anything
"""
import json
import replicate
import requests

from flask import jsonify, abort, request
from btb_ai import app


""" 
@app.before_request
def send_image_to_process():
    "Imitation of a middleware"
    if request.path == '/process_image':
        # Assuming the image file is located on the server
        data = {'image_path':'imgs/photo_5440411542173633301_y.jpg'}
        response = requests.post('http://localhost:5000/process_image', data=data) """


@app.route('/process_image', methods=['POST', 'GET'])
def process_image():
    # TODO: img_path as request data
    # uncomment use the API, limited credits so using the dummy_response.json for now.
    """     image_path = 'imgs/photo_5440411542173633301_y.jpg'
    output = replicate.run(
            "idea-research/ram-grounded-sam:80a2aede4cf8e3c9f26e96c308d45b23c350dd36f1c381de790715007f1ac0ad",
            input={"input_image": open(image_path, "rb")}
        ) """
    with open("dummy_response.json") as f:
        output = json.load(f)
        print("called")
    return jsonify({"tags": output["tags"]})

@app.route('/')
def index():
    return 'Hello'
    #abort(404)



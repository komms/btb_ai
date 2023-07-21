# btb_ai/btb_ai/__init__.py

from flask import Flask

# Create the Flask application object
app = Flask(__name__)

# Import the views module to register the routes
from btb_ai.views.ai_model import *

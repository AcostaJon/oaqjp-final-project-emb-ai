"""import flask and emotion detector function"""
from flask import Flask
from emotion_detection import emotion_detector

app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route("/")
def hello_world():
    """route for root URL (/)"""
    return {"message" : emotion_detector("I love my life")}, 200

# error 404
@app.errorhandler(404)
def api_not_found():
    """Function error handler"""
    return {"message" : "None"}, 404

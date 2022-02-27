from flask import Blueprint, request, current_app as app
import flask
import requests
from app_utils import keys_missing, BACKEND_URL, COOKIE_ROLE

questions = Blueprint('questions', __name__)

@questions.route("/api/questions/new", methods=["POST"])
def question_new():
    """
    Accepts a new question to be inserted into the question bank.
    
    Example JSON Body:
        {
            "professorID": "professorID_001",
            "title": "Double it",
            "description": "Write a function named `doubleIt`...",
            "topic": "functions",
            "difficulty": "easy",
            "testCases": [{
                "functionCall": "doubleIt(3)",
                "expectedOutput": 6,
                "type": "int"
            }]
        }
    
    Returns:
        ({
            "questionID": "questionID_001"
        }, 201)
    """
    data = request.json
    app.logger.debug(data)
    # validate all keys exist
    req_keys = ["title", "description", "topic", "difficulty", "testCases"]
    if keys_missing(req_keys, data):
        return flask.jsonify({"error": "missing keys in form data"}), 400

    if keys_missing(["functionCall", "expectedOutput", "type"], data["testCases"]):
        return flask.jsonify({"error": "missing keys in testCases"}), 400

    return flask.jsonify({"status": "Good, all keys present. Backend not reached."}), 200

    # hand off to database to insert 
    r = requests.post(f"{BACKEND_URL}/new_question", json=data)

    if r.status_code in [200, 201]:
        return r.status_code

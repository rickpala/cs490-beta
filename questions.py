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
            "category": "functions",
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
    print(data)
    # validate all keys exist
    req_keys = ["professorID", "title", "description", "category", "difficulty", "testCases"]
    if keys_missing(req_keys, data):
        return flask.jsonify({"error": "missing keys in form data"}), 400

    if keys_missing(["functionCall", "expectedOutput", "type"], data["testCases"]):
        return flask.jsonify({"error": "missing keys in testCases"}), 400

    # hand off to database to insert 
    r = requests.post(f"{BACKEND_URL}/new_question", json=data)
    return flask.jsonify(r.json()), r.status_code
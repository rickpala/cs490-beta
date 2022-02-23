
from flask import Blueprint, request, current_app as app
import flask
import requests
from typing import List, Dict

questions = Blueprint('questions', __name__)

# Constants
BACKEND_URL = "https://cs100-testing-backend.herokuapp.com"
COOKIE_ROLE = "Role"

def keys_missing(req_keys: List[str], data: Dict) -> bool:
    if not isinstance(req_keys, List):
        return False
    if len(req_keys) != len(data):
        return False
    """Returns true if any keys are missing from data."""
    return not all(key in data for key in req_keys)

@questions.route("/api/questions/new", methods=["POST"])
def question_new():
    data = request.data
    app.logger.debug(data)
    # validate all keys exist
    req_keys = ["title", "description", "topic", "difficulty", "testCases"]
    if (keys_missing(req_keys, data) or 
        keys_missing(["callSignature", "answer"], data["testCases"])):
        return jsonify({"error": "missing keys"}), 400

    # hand off to database to insert 
    r = requests.post(f"{BACKEND}/new_question", json=data)

    if r.status_code in [200, 201]:
        return r.status_code

@questions.route("/api/questions/show", methods=["GET"])
def show_questions():
    r = requests.get(f"{BACKEND}/all_questions")
    pass 

@questions.route("/api/exam/new", methods=["POST"])
def new_exam():
    """Accepts a list of questionIDs to create an exam from."""
    pass

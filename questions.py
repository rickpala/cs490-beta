from flask import Blueprint, request, current_app as app
import flask
import requests
from app_utils import keys_missing, BACKEND_URL, COOKIE_ROLE

questions = Blueprint('questions', __name__)

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


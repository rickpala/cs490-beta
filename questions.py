from flask import Blueprint, request, current_app as app
import flask
import requests
from app_utils import keys_missing, BACKEND_URL, COOKIE_ROLE

questions = Blueprint('questions', __name__)

@questions.route("/api/questions/new", methods=["POST"])
def question_new():
    data = request.json
    app.logger.debug(data)
    # validate all keys exist
    req_keys = ["title", "description", "topic", "difficulty", "testCases"]
    if keys_missing(req_keys, data):
        return flask.jsonify({"error": "missing keys"}), 400

    if keys_missing(["callSignature", "answer", "type"], data["testCases"]):
        pass # TODO: Validate testCases

    return flask.jsonify({}), 200

    # hand off to database to insert 
    r = requests.post(f"{BACKEND_URL}/new_question", json=data)

    if r.status_code in [200, 201]:
        return r.status_code

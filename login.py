from flask import Blueprint, request, current_app as app
import flask
import requests

login = Blueprint('login', __name__)
json_headers = {"Content-Type": "application/json"}
@login.route('/api/login', methods=["POST"])
def api_login():
    # receive body from frontend,
    body = flask.request.json
    app.logger.debug(body)

    # handoff to backend for validation
    backend = "https://cs100-testing-backend.herokuapp.com/validate_login"
    r = requests.post(backend, json=body, headers=json_headers)

    # grant/deny access via JSON credentials
    return flask.jsonify(r.text)


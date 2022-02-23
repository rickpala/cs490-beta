from flask import Blueprint, request, current_app as app
import flask
import requests

login = Blueprint('login', __name__)

@login.route('/api/login', methods=["POST"])
def api_login():
    # receive body from frontend,
    body = flask.request.data

    # handoff to backend for validation
    backend = ("https://cs100-testing-backend.herokuapp.com/validate_login")
    r = requests.post(backend, json=body)

    # grant/deny access via JSON credentials
    return r.json()


from flask import Blueprint, request, current_app as app
import flask
import requests

login = Blueprint('login', __name__)

@login.route('/api/login', methods=["POST"])
def api_login():
    # receive body from frontend,
    app.logger.info(request.data)
    app.logger.info(request.json)

    # handoff to backend for validation
    backend = ("https://afsaccess4.njit.edu/~ps852/"
               "alpha/functionality/validate_login.php")
    r = requests.post(backend, json=request.json)

    # check for student/teacher/error
    app.logger.info(r.status_code)

    # grant/deny access via JSOownedN credentials
    return r.json()


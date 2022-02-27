from typing import Dict, List

import flask
import requests
from flask import Blueprint
from flask import current_app as app
from flask import request

from app_utils import *

exams = Blueprint('exams', __name__)

@exams.route("/api/questions/show", methods=["GET"])
def show_questions():
    r = requests.get(f"{BACKEND_URL}/question_bank")
    return r.json, r.status_code

@exams.route("/api/exam/new", methods=["POST"])
def new_exam():
    """
    Creates a new exam from a list of supplied questions.
    
    Example JSON body:
        {
            "professorID": "professorID_001",  /* via Cookie */
            "questions": [{
                "questionID": "questionID_001",
                "points": 10
            },
            {
                "questionID": "questionID_002",
                "points": 6
            }]
        } 

    Returns:
        ({
            "examID": "examID_008" /* after db insert */
        }, 201)
    """
    # TODO: Assign exam to specific students
    backend_endpoint = f"{BACKEND_URL}/new_exam"
    data = request.json
    req_keys = {"root": ["professorID", "questions"],
                "questions": ["questionID", "points"]}

    if not data:
        return flask.jsonify({"error": "missing JSON data"}), 400
    if keys_missing(req_keys["root"], data):
        return flask.jsonify({"error": "missing keys in form data"}), 400
    if keys_missing(req_keys["questions"], data.get("questions")):
        return flask.jsonify({"error": "missing keys in questions"}), 400

    try:  # Reach backend to insert into DB
        app.logger.info(f"Attempting to communicate to {backend_endpoint}")
        # TODO: Convert `data` into 3NF for individual insertion to backend
        r = requests.post(f"{backend_endpoint}", json=data)
        app.logger.info(f"Backend returned {r.status_code}")
        return flask.jsonify({"status": r.status_code}), r.status_code
    except Exception as e:
        app.logger.debug(e)
        return flask.jsonify({"error": "backend didn't return valid response"})

@exams.route("/api/exam/submit", methods=["POST"])
def submit_exam():
    """
    Accepts a student's exam submission.
    
    Expected JSON body:
        {
            “examID”: “examID_001”,
            “studentID”: “studentID_001”,
            “submission”: [{
                “questionID”: “questionID_001”,
                “response”: “def foo(x):\n    return x”
            },
            {
                “questionID”: “questionID_002”,
                “response”: “def foo(x):\n    return x”
            }]
        }

    Returns:
        ({
            "submissionID": "submissionID_001" /* after db insert */
        }, 201)
    """
    # Constants
    data = request.json
    backend_endpoint = f"{BACKEND_URL}/submit_exam"
    req_keys = {"root": ["examID", "studentID", "submission"],
                "submission": ["questionID", "response"]}

    if not data:
        return flask.jsonify({"error": "missing POSTed JSON"}), 400
    elif keys_missing(req_keys["root"], data):
        return flask.jsonify({"error": "missing keys in form data"}), 400
    elif keys_missing(req_keys["submission"], data.get("submission")):
        return flask.jsonify({"error": "missing keys in submission"}), 400

    try:  # Reach backend to insert into DB
        app.logger.info(f"Attempting to communicate to {backend_endpoint}")
        # TODO: Insert new submission as [examID, studentID, submission]
        # TODO: Insert individual question submissions 
        # TODO: Convert `data` into 3NF for individual insertion to backend

        r = requests.post(backend_endpoint, json=data)
        app.logger.info(f"Backend returned HTTP {r.status_code}")
        return flask.jsonify({"status": r.status_code}), 400
    except Exception as e:
        app.logger.debug(e)
        return flask.jsonify({"error": "backend didn't return valid response"})

from flask import Blueprint, request, current_app as app
from typing import List, Dict
from app_utils import *
import flask
import requests

exams = Blueprint('exams', __name__)

@exams.route("/api/questions/show", methods=["GET"])
def show_questions():
    r = requests.get(f"{BACKEND_URL}/all_questions")
    return 501  # Not Implemented

@exams.route("/api/exam/new", methods=["POST"])
def new_exam():
    """
    Creates a new exam from a list of supplied questions.
    
    Example JSON body:
        {
            "teacherID": "teacherID_001",  /* via Cookie */
            "assignees": [
                "studentID_001",
                "studentID_002",
                ...
            ],
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
    return 501  # Not Implemented


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
    return 501  # Not Implemented

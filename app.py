from flask import Flask, request
from login import login
from sitemap import sitemap
from questions import questions
from exams import exams
import logging
import requests
app = Flask(__name__)
app.register_blueprint(login)
app.register_blueprint(sitemap)
app.register_blueprint(questions)
app.register_blueprint(exams)

@app.route("/api/__health")
def health():
    return "OK"

@app.route('/api/teapot', methods=["GET", "POST"])
def test_teapot():
    """Makes a request to another web server on behalf of the user."""
    r = requests.get("https://shielded-ridge-12044.herokuapp.com")
    return r.text

if __name__ == '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
    app.run(host='0.0.0.0')

from flask import Flask, request
from login import login
from sitemap import sitemap
import logging
app = Flask(__name__)
app.register_blueprint(login)
app.register_blueprint(sitemap)

@app.route("/api/__health")
def health():
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
else:
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
    app.run()

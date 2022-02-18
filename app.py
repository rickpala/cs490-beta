from flask import Flask, request
app = Flask(__name__)

@app.route("/api/hello")
def hello_world():
    return "hello!"

@app.route("/api/body", methods=["POST"])
def test_body():
    body = request.body
    return str(body)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

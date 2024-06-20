from app import app
from flask import g
import threading

counter_lock = threading.Lock()
request_count = 0


@app.before_request
def before_request():
    global request_count
    with counter_lock:
        request_count += 1
    g.request_count = request_count


@app.route("/", methods=["GET"])
def hello():
    return f"{g.request_count}"


@app.route("/api/people", methods=["GET"])
def people():
    return "THIS IS PEOPLE PAGE"

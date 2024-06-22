from app import app
import os
import redis
import uuid
from flask import make_response, session, send_file

app.secret_key = os.getenv("SECRET_KEY")

r = redis.Redis(host="localhost", port=6379)


@app.before_request
def count_requests():
    if "user_id" not in session:
        session["user_id"] = str(uuid.uuid1())

    user_id = session["user_id"]

    r.incr(user_id)


@app.route("/")
def index():
    return send_file("../static/index.html")


@app.route("/api", methods=["GET"])
def api():
    response = make_response({"msg": "request_fullfilled"})

    return response


@app.route("/api/people", methods=["GET"])
def people():
    return "THIS IS PEOPLE PAGE"

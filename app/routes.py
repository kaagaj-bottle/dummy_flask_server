from app import app
import os
import uuid
from rq.job import Job
from flask import jsonify, make_response, session, send_file, request
from app.connections import r_conn, queue
from app.utils import fetch_urls_from_db, push_url_text_from_web

app.secret_key = os.getenv("SECRET_KEY")


@app.route("/")
def index():
    return send_file("../static/index.html")


@app.route("/api/push_url", methods=["POST"])
def push_url():

    url = request.form["url"]
    if "user_id" not in session:
        session["user_id"] = str(uuid.uuid1())

    user_id = session["user_id"]
    r_conn.lpush(user_id, url)
    queue.enqueue(push_url_text_from_web, args=(url,), job_id=url)

    return jsonify({"msg": "success"})


@app.route("/api/get_url")
def get_url():

    if "user_id" not in session:
        response = make_response({"url": []})
        return response
    user_id = session["user_id"]
    urls = fetch_urls_from_db(user_id)

    return jsonify({"urls": urls})


@app.route("/api/get_url_text")
def get_url_text():
    url = request.form["url"]

    job = Job.fetch(id=url, connection=r_conn)

    return jsonify({url: job.return_value()})


@app.route("/api/people", methods=["GET"])
def people():
    return "THIS IS PEOPLE PAGE"

from app import app
from flask import g, jsonify, make_response, request


@app.route("/", methods=["GET"])
def hello():
    request_count = int(request.cookies.get("request_count", "0"))

    request_count = request_count + 1
    response = make_response({"request_count": request_count})
     
    response.set_cookie(
        "request_count", str(request_count), max_age=24 * 60 * 60, secure=False
    )
    print(response.headers)
    return response


@app.route("/api/people", methods=["GET"])
def people():
    return "THIS IS PEOPLE PAGE"

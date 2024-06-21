from app import app
from flask import g, jsonify, make_response, request, send_file


@app.route("/")
def index():
    return send_file('../static/index.html')


@app.route("/api", methods=["GET"])
def api():
    request_count = int(request.cookies.get("request_count", "0"))

    request_count +=1
    print("request_count: ",request_count)
    response = make_response({"msg":"request fullfilled" })

    response.set_cookie(
        "request_count",
        str(request_count),
        max_age=24 * 60 * 60,
        secure=False,
        path="/",
        httponly=False,
        domain=".127.0.0.1",
        samesite="None",
    )

    return response


@app.route("/api/people", methods=["GET"])
def people():
    return "THIS IS PEOPLE PAGE"

from flask import Flask
from flask_cors import CORS


app = Flask(__name__)

CORS(
    app,
    origins="*",
    supports_credentials=True,
)


from app import routes

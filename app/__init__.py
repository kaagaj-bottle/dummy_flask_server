from flask import Flask, g
from flask_cors import CORS
import threading



app = Flask(__name__)

CORS(app, origins="*")



from app import routes

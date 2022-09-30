from flask import Flask, redirect, url_for, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*':{'origins': 'http://localhost:8080', "allow_headers" : "Access-Control-Allow-Origin"}})

@app.route("/home", methods=['GET', 'POST'])
def home():
    return "This message is a test for backend."

@app.route("/")
def default():
    return redirect(url_for("home"))
from flask import Flask, redirect, url_for, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*':{'origins': 'http://localhost:8080', "allow_headers" : "Access-Control-Allow-Origin: *"}})

@app.route("/home", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return "POST method test."
    else:
        return "This message is a test for backend."

@app.route("/login", methods=['POST'])
def login():
    firstName = request.form
    print(firstName)
    return firstName

@app.route("/")
def default():
    return redirect(url_for("home"))
from flask import Flask, redirect, url_for, jsonify, request
from flask_cors import CORS, cross_origin
import mysql.connector

app = Flask(__name__)
app.config.from_object(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})

#conn = mysql.connector.connect(user='localhost', password='Resumaftif', host='ds13475.dreamservers.com', database='fitfamdb')
#conn.close()

@app.route("/home", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return "POST method test."
    else:
        return "This message is a test for backend."

@app.route("/login", methods=['POST'])
def login():
    info = request.get_json(silent=True)
    firstName = info['first']
    lastName = info['last']
    email = info['email']
    password = info['password']

    print(f"\nUser: {firstName} {lastName}\nEmail: {email}\nPassword: {password}\n")
    return info

@app.route("/")
def default():
    return redirect(url_for("home"))
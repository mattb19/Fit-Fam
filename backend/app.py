import json
from xmlrpc.client import ResponseError
from flask import Flask, redirect, url_for, jsonify
from flask_cors import CORS
from flask import request
from flask import Flask, redirect, url_for, jsonify, request
from flask_cors import CORS, cross_origin
#import mysql.connector


app = Flask(__name__)
app.config.from_object(__name__)


CORS(app, resources={r'/*':{'origins': '*'}})

item2 = []

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

@app.route("/security_questions", methods=['POST'])
def securityQuestions():
    info = request.get_json(silent=True)
    questionStringA = info['secQuestion1']
    answerStringA = info['answer1']
    questionStringB = info['secQuestion2']
    answerStringB = info['answer2']
    print(f"\nSecurity Question 1: {questionStringA} \nanswer1: {answerStringA} \nSecurity question2: {questionStringB} \nAnswer2: {answerStringB}")
    return info

@app.route("/")
def default():
    return redirect(url_for("home"))

@app.route("/post", methods=['GET','POST'])
def post():

    # data is the post data put in jsonified format
    data = request.get_json(force=True)

    # making dict object for post data
    item = {
        'title': data.get('title'),
        'description': data.get('description'),
        'image': data.get('image')
        }
    item2.append(item)
    return item
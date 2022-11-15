from flask import Flask, redirect, url_for, request, session, jsonify
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from werkzeug.security import generate_password_hash, check_password_hash
from Database import db
from data import Data
#import mysql.connector


def register_extensions(app):
    # this and the next function are to resolve a circular import issue
    db.init_app(app)

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    return app

app = create_app(Config)
migrate = Migrate(app, db)


from models import *    # IMPORT THE MODELS


CORS(app, resources={r'/*':{'origins': '*'}})

item2 = []

@app.route("/posts", methods=['GET', 'POST'])
def posts():
    print(item2)
    return item2


@app.route("/home", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return "POST method test."
    else:
        return "This message is a test for backend."


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        info = request.get_json(silent=True)
        userEmail = info['email']
        userPassword = info['password']
        user = User.query.filter_by(email = userEmail).first()
        if user is None or not check_password_hash(user.password, userPassword):
            return jsonify("invalid"), 401
        return jsonify("valid"), 200


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        info = request.get_json(silent=True)
        first = info['first']
        last = info['last']
        email = info['email']
        password = generate_password_hash(info['password'])
        user = User.query.filter_by(email = email).first()
        if user is None:
            user = User(firstName=first, lastName=last, email=email, password=password)
            db.session.add(user)
            db.session.commit()
        else:
            return jsonify("invalid"), 401
        return jsonify("valid"), 200


@app.route("/security_questions", methods=['POST'])
def securityQuestions():
    info = request.get_json(silent=True)
    questionStringA = info['secQuestion1']
    answerStringA = info['answer1']
    questionStringB = info['secQuestion2']
    answerStringB = info['answer2']
    userEmail = info['userEmail']
    user = User.query.filter_by(email = userEmail).first()
    securityQuestions = SecurityQuestions(userId = user.id, Question1 = questionStringA, Answer1 = answerStringA, Question2 = questionStringB, Answer2 = answerStringB)
    db.session.add(securityQuestions)
    db.session.commit()
    print(f"\nSecurity Question 1: {questionStringA} \nanswer1: {answerStringA} \nSecurity question2: {questionStringB} \nAnswer2: {answerStringB}")
    return info

@app.route("/")
def default():
    return redirect(url_for("login"))

@app.route("/post", methods=['GET','POST'])
def post():

    # data is the post data put in jsonified format
    data = request.get_json(force=True)

    # making dict object for post data
    item = {
        'title': data.get('title'),
        'description': data.get('description'),
        'image': data.get('image'),
        'userId': data.get('userId')
        }
    item2.append(item)
    print(item)
    print(item2)
    return item
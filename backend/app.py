from flask import Flask, redirect, url_for, request, session, jsonify
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.urls import url_parse
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from Database import db
from flask_session import Session
from data import Data
#import mysql.connector

from flask_jwt_extended import create_access_token
from flask_jwt_extended import current_user
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

# dependencies:
# pip install flask-jwt-extended

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
jwt = JWTManager(app)
# login_manager = LoginManager(app)
# login_manager.login_view = 'login'
# login_manager.init_app(app)

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'super secret key'
app.config.update(SESSION_COOKIE_SAMESITE="None", SESSION_COOKIE_SECURE=True)
Session(app)

app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
JWT_TOKEN_LOCATION=['cookies']


from models import *    # IMPORT THE MODELS


CORS(app, resources={r'/*':{'origins': '*'}})

item2 = []

@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.filter_by(id=identity).one_or_none()


@app.route("/posts", methods=['GET', 'POST'])
@jwt_required()
def posts():
    print(item2)
    return item2


@app.route("/home", methods=['GET', 'POST'])
#@jwt_required()
def home():
    if request.method == 'POST':
        return "POST method test."
    else:
        return "This message is a test for backend."

# @login_manager.user_loader
# def load_user(id):
#     user = User.query.filter_by(email = id).first()
#     return user

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        info = request.get_json(silent=True)
        userEmail = info['email']
        userPassword = info['password']
        print('email:', userEmail, '\tpassword:', userPassword)
        user = User.query.filter_by(email = userEmail).first()
        if user is None or not check_password_hash(user.password, userPassword):
            return jsonify("Wrong username or password"), 401
        #login_user(user) # this is where you can add cookie using remember parameter of the login_user() function
        # login_user(user, remember=True)
        # session['usr'] = userEmail
        print('logged in----------------------------')
        # print('User:', current_user)
        access_token = create_access_token(identity=user)
        return jsonify(access_token=access_token)


@app.route("/logout")
@jwt_required()
def logout():
    data = Data()
    data.setEmail('')
    return redirect(url_for('login'))

@app.route("/signup", methods=['GET', 'POST'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def signup():
    if request.method == 'POST':
        data = Data()   # remove
        info = request.get_json(silent=True)
        first = info['first']
        last = info['last']
        email = info['email']
        password = generate_password_hash(info['password'])
        session["email"] = email
        user = User.query.filter_by(email = email).first()
        if user is None:
            user = User(firstName=first, lastName=last, email=email, password=password)
            db.session.add(user)
            db.session.commit()
            data.setEmail(email)   # remove
        else:
            print('Email already in use.')

        print(f"\nUser: {first} {last}\nEmail: {email}\nPassword: {password}\n")
        
        # probably won't need to use tokens, just sessions
        access_token = create_access_token(identity=user)
        print('token;', access_token)
        print('signup session:', session)
        return jsonify(access_token=access_token)


@app.route("/security_questions", methods=['POST'])
#@jwt_required()
def securityQuestions():
    #print('Current User:')
    #print(current_user)
    data = Data()   # remove
    info = request.get_json(silent=True)
    #userEmail = data.getEmail()   # remove
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
@jwt_required()
def default():
    return redirect(url_for("posts"))

@app.route("/post", methods=['GET','POST'])
@jwt_required()
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
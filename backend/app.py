from flask import Flask, redirect, url_for, request, flash
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.urls import url_parse
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from Database import db
from models import User
from models import Groups
from data import Data
#import mysql.connector
import sqlite3

def register_extensions(app):
    # this and the next function are to resolve a curcular import issue
    db.init_app(app)

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    return app

app = create_app(Config)
migrate = Migrate(app, db)
# login_manager = LoginManager(app)
# login_manager.login_view = 'login'
# login_manager.init_app(app)
# app.config['SESSION_TYPE'] = 'filesystem'
# app.config['SECRET_KEY'] = 'super secret key'
# app.config.update(SESSION_COOKIE_SAMESITE="None", SESSION_COOKIE_SECURE=True)
# Session(app)

from models import *    # IMPORT THE MODELS

CORS(app, resources={r'/*':{'origins': '*'}})

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("app.db")
    except sqlite3.error as e:
        print(e)
    return conn

Item2 = []
postObjList = []
retrievalStepSize = 10
feedPosition = 0
targetGroup = 0
targetPersonsStr = ""

#target persons assignment will be
#" AND poster = targetPersons"

@app.route("/feedmeta", methods=['GET', 'POST'])
def feedMeta():
    global postObjList
    postObjList = []
    global feedPosition
    conn = db_connection()
    cursor = conn.cursor()
    cursor = conn.execute(
        'SELECT postId FROM Posts'
    )
    feedPosition = len(cursor.fetchall())
    if feedPosition is None:
        feedPosition = 0
    else:
        feedPosition -= retrievalStepSize
    return "Feed position set"

@app.route("/posts", methods=['GET', 'POST'])
def posts():
    global feedPosition
    conn = db_connection()
    cursor = conn.cursor()
    global postObjList
    if feedPosition > 0:
        cursor = conn.execute(
            "WITH Posts_Numbered AS (SELECT *, ROW_NUMBER() OVER(ORDER BY _ROWID_) RowNum FROM Posts) SELECT Posts_Numbered.*, User.firstName, User.lastName, User.nickname FROM Posts_Numbered LEFT JOIN User ON Posts_Numbered.poster = User.id WHERE RowNum > " + str(feedPosition) + " AND RowNum <= " + str(feedPosition+retrievalStepSize) + " AND groupAssociation = " + str(targetGroup) + targetPersonsStr
        )
        
        tmpPostObjList = ([
            dict(
                postId=row[0],
                postDateTime=row[1],
                poster=row[2],
                groupAssociation=row[3],
                description=row[4],
                postTags=row[5],
                postImage=row[6],
                postLikes=row[7],
                #feedRow=row[8],
                #postLikeAssociation,
                postFirstName=row[9],
                postLastName=row[10],
                postNickname=row[11]

                #this data needs to be pulled from key relations in other tables
            )
            for row in cursor.fetchall()
        ])
        tmpPostObjList.reverse()
        postObjList = postObjList + tmpPostObjList
        feedPosition -= retrievalStepSize
    #print(postObjList[0])
    return postObjList

@app.route("/home", methods=['GET', 'POST'])
# @login_required
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
            '''
            flash('Invalid username or password')
            return redirect(url_for('login'))
            '''
            print('wrong user/password or user doesn\'t exist')
            return 'login'
        #login_user(user) # this is where you can add cookie using remember parameter of the login_user() function
        # login_user(user, remember=True)
        # session['usr'] = userEmail
        print('logged in----------------------------')
        # print('User:', current_user)
        return 'home'

@app.route("/logout")
def logout():
    data = Data()
    data.setEmail('')
    return redirect(url_for('login'))

@app.route("/signup", methods=['POST'])
def signup():
    data = Data()
    info = request.get_json(silent=True)
    first = info['first']
    last = info['last']
    email = info['email']
    password = generate_password_hash(info['password'])
    #session["email"] = email
    user = User.query.filter_by(email = email).first()
    if user is None:
        user = User(firstName=first, lastName=last, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        data.setEmail(email)
    else:
        print('Email already in use.')
        return redirect(url_for('signup'))

    print(f"\nUser: {first} {last}\nEmail: {email}\nPassword: {password}\n")
    #return redirect(url_for('securityQuestions'))
    return info


@app.route("/security_questions", methods=['POST'])
def securityQuestions():
    data = Data()
    info = request.get_json(silent=True)
    userEmail = data.getEmail()
    questionStringA = info['secQuestion1']
    answerStringA = info['answer1']
    questionStringB = info['secQuestion2']
    answerStringB = info['answer2']
    user = User.query.filter_by(email = userEmail).first()
    securityQuestions = SecurityQuestions(userId = user.id, Question1 = questionStringA, Answer1 = answerStringA, Question2 = questionStringB, Answer2 = answerStringB)
    db.session.add(securityQuestions)
    db.session.commit()
    print(f"\nSecurity Question 1: {questionStringA} \nanswer1: {answerStringA} \nSecurity question2: {questionStringB} \nAnswer2: {answerStringB}")
    return info

@app.route("/")
@login_required
def default():
    return redirect(url_for("posts"))

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
    Item2.append(item)
    print(item)
    return item


@app.route("/groups", methods=['GET', 'POST'])
def createGroup():
    info = request.get_json(silent=True)
    userId = 1
    groupId = 2
    groupName = "Trenything is possible"
    group = Groups(groupName=groupName, groupOwner=userId)
    db.session.add(group)
    db.session.commit()


    print(f"\nGroup: {groupId} {groupName}\nCreator: {userId}")
    return "group feed will display here"
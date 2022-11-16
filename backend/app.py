from flask import Flask, redirect, url_for, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from werkzeug.security import generate_password_hash, check_password_hash
from Database import db
#import mysql.connector
import sqlite3


def register_extensions(app):
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

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("app.db")
    except sqlite3.error as e:
        print(e)
    return conn


Item2 = []

@app.route("/posts", methods=['GET', 'POST'])
def posts():
    conn = db_connection()
    cursor = conn.cursor()
    cursor = conn.execute("SELECT * FROM Posts")

    postObjList = [
        dict(
            postId=row[0],
            postDateTime=row[1],
            poster=row[2],
            groupAssociation=row[3],
            description=row[4],
            postTags=row[5],
            postImage=row[6],
            postLikes=row[7]#,
            # postLikeAssociation,
            # postNickName

            #this data needs to be pulled from key relations in other tables
        )
        for row in cursor.fetchall()
    ]

    return postObjList

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
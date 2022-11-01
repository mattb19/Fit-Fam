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
#import mysql.connector

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

CORS(app, resources={r'/*':{'origins': '*'}})

login = LoginManager(app)
login.login_view = 'login'

item2 = []

@app.route("/posts", methods=['GET', 'POST'])
def posts():
    print(item2)
    return item2

@app.route("/home", methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        return "POST method test."
    else:
        return "This message is a test for backend."

@app.route("/login", methods=['POST'])
def login():
    # if current_user.is_authenticated:
    #     return redirect(url_for('home'))
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
        return redirect(url_for('login'))
    #login_user(user) # this is where you can add cookie using remember parameter of the login_user() function
    print('logged in----------------------------')
    return redirect(url_for('home'))
    

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/signup", methods=['POST'])
def signup():
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
        print('Email already in use.')
        #return redirect(url_for('signup'))

    print(f"\nUser: {first} {last}\nEmail: {email}\nPassword: {password}\n")
    #return redirect(url_for('security_questions'))
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
    item2.append(item)
    print(item)
    print(item2)
    return item
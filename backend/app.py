import json
import Post as PostFile
from xmlrpc.client import ResponseError
from flask import Flask, redirect, url_for, jsonify, request
from flask_cors import CORS, cross_origin
#import mysql.connector


app = Flask(__name__)
app.config.from_object(__name__)


CORS(app, resources={r'/*':{'origins': '*'}})

item2 = []

feedPostList = []

@app.route("/home", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return "POST method test."
    else:
        return "This message is a test for backend."

tmp = ["John Doe","Jane Doe","Joe Schmo","Thomas Tugman","Jackson Pot","Phil Smith"]
#list used for psuedo data generation

@app.route("/feed", methods=['GET', 'POST'])
def posts():
    if request.method == 'POST':
        tmpFeedPostList = []

        for i in range(10):
            postItem = PostFile.Post(1,0,"timeHere","","Bicepts:Curls:Weights",0)
            #postItem.postText = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In odio mauris, sollicitudin ac consequat a, pretium non mauris. Nullam elit turpis, fringilla efficitur pellentesque sed, fermentum sed nulla. Donec vitae elit nec nisl luctus sodales nec porta turpis. Nunc pulvinar a mi at mattis. Nunc quis mi in arcu lobortis pellentesque non in dui. Mauris ut justo maximus, dignissim diam a, dignissim felis. Fusce efficitur accumsan ex id porta. Proin elementum convallis tellus id malesuada. Morbi et fermentum velit. In massa orci, iaculis tincidunt erat sed, rhoncus mattis erat. Aenean at tristique urna."
            postItem.postText = "Lorem ipsum"
            tmpFeedPostList.append(postItem)
        #Above block is psudo data generation loop

        for i in tmpFeedPostList:
            feedPostList.append(i.__dict__)

        return feedPostList
    else:
        tmpFeedPostList = []

        for i in range(10):
            postItem = PostFile.Post(1,0,"timeHere","","Bicepts:Curls:Weights",0)
            #postItem.postText = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In odio mauris, sollicitudin ac consequat a, pretium non mauris. Nullam elit turpis, fringilla efficitur pellentesque sed, fermentum sed nulla. Donec vitae elit nec nisl luctus sodales nec porta turpis. Nunc pulvinar a mi at mattis. Nunc quis mi in arcu lobortis pellentesque non in dui. Mauris ut justo maximus, dignissim diam a, dignissim felis. Fusce efficitur accumsan ex id porta. Proin elementum convallis tellus id malesuada. Morbi et fermentum velit. In massa orci, iaculis tincidunt erat sed, rhoncus mattis erat. Aenean at tristique urna."
            postItem.postText = "Lorem ipsum"
            tmpFeedPostList.append(postItem)
        #Above block is psudo data generation loop

        for i in tmpFeedPostList:
            feedPostList.append(i.__dict__)
            
        return jsonify(feedPostList)

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

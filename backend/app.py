import json
from xmlrpc.client import ResponseError
from flask import Flask, redirect, url_for, jsonify
from flask_cors import CORS
from flask import request

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*':{'origins': '*'}})

item2 = []

@app.route("/home", methods=['GET', 'POST'])
def home():
    return item2

@app.route("/")
def default():
    return redirect(url_for("home"))

@app.route("/post", methods=['GET','POST'])
def post():

    # data is the post data put in jsonified format
    data = request.get_json(force=True)

    #making dict object for post data
    item = {
        'title': data.get('title'),
        'description': data.get('description'),
        'image': data.get('image')
        }
    item2.append(item)
    return item
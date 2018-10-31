from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

import db

@app.route("/")
def hello():
    return "Hello World!"


@app.route('/testdb')
def test():
    return db.test()

@app.route('/request', methods=['post'])
def receivePost():
    return db.acceptPost(request)

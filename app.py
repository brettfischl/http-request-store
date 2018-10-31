from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

import db

@app.route("/")
def hello():
    return "Hello World!"


@app.route('/testdb')
def test():
    return db.test()

@app.route('/request', methods=['post'])
def receivePost():
    return db.receivePost(request)

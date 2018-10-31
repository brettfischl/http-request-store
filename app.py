from flask import Flask
from flask import request, make_response

app = Flask(__name__)

import db

def any_response(data):
    response = make_response(data)
    origin = request.headers['Origin']

    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route("/")
def hello():
    return "Hello World!"


@app.route('/testdb')
def test():
    return db.test()

@app.route('/request', methods=['post'])
def receivePost():
    # data = request.data
    return any_response(db.receivePost(request))

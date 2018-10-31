from flask import Flask
from flask import request
app = Flask(__name__)

import db

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
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
    return db.receivePost(request)

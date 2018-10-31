from flask import Flask

app = Flask(__name__)

import db

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', 'http://localhost:8000')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  response.headers.add('Access-Control-Allow-Credentials', 'true')
  return response

@app.route("/")
def hello():
    return "Hello World!"


@app.route('/testdb')
def test():
    return db.test()

@app.route('/request', methods=['post'])
@app.after_request
def receivePost():
    return db.receivePost(request)

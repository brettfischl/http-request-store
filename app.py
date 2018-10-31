from flask import Flask
from flask import request, make_response

app = Flask(__name__)

import db

def any_response(data):
  ALLOWED = ['http://localhost:8888']
  response = make_response(data)
  origin = request.headers['Origin']
  if origin in ALLOWED:
    response.headers['Access-Control-Allow-Origin'] = origin
  return response

@app.route("/")
def hello():
    return "Hello World!"


@app.route('/testdb')
def test():
    return db.test()

@app.route('/request', methods=['post'])
@crossdomain(origin='*')
def receivePost():
    # data = request.data
    return any_response(db.receivePost(request))

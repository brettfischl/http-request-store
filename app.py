from flask import Flask
from flask import request
app = Flask(__name__)

import db

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
    return db.receivePost(request)

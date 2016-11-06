#!/usr/local/python
# coding = utf-8

from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer','42')
    return response
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello,%s!' % name
@app.route('/baidu')
def baidu():
    return redirect('https://www.baidu.com')




if __name__ == '__main__':
    app.run(host=app.config.get('HOST',None),port=app.config.get('PORT',None))

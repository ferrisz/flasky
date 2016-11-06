#!/usr/local/python
# coding = utf-8

from flask import Flask, render_template
from flask import request
from flask import make_response
from flask import redirect
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECERT_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)

moment = Moment(app)



class NameForm(Form):
    name = StringField('What is your name?',validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/')
def index():
    return render_template('index.html',current_time=datetime.utcnow())


@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)
@app.route('/baidu')
def baidu():
    return redirect('https://www.baidu.com')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(host=app.config.get('HOST',None),port=app.config.get('PORT',None))

#!/usr/local/python
# coding = utf-8

from flask import Flask, render_template, session, redirect, url_for, flash
from flask import request
from flask import make_response
# from flask import redirect
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECERT_KEY'] = 'hard to guess string'
app.config['WTF_CSRF_ENABLED'] = False

bootstrap = Bootstrap(app)
moment = Moment(app)


class NameForm(Form):
    name = StringField('What is your name?',validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_server_error(e):
    return render_template('500.html'), 500

@app.route('/', methods=['GET','POST'])
def index():
    # name = None
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        # name = form.name.data
        session['name'] = form.name.data
        # form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html',form=form,name=session.get('name'))


@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)




if __name__ == '__main__':
    app.run(host=app.config.get('HOST',None),port=app.config.get('PORT',None))

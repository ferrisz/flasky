#!/usr/local/python
# coding = utf-8

import os
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
from flask_sqlalchemy import SQLAlchemy
from flask_script import Shell,Manager

basedir = os.path.abspath(os.path.dirname(__file__))

# DatabaseConfig
server_type = 'mysql'  # mysql pg
server_host = '119.29.136.24'
server_port = '3306'
server_user = 'flasky'
server_pass = 'flasky'
server_db = 'flasky'
server_charset = 'utf8mb4'

# DefineDatebaseType
serverHeader = ''
if server_type == 'mysql':
    serverHeader = 'mysql+pymysql://'
elif server_type == 'pg':
    serverHeader = 'postgresql://'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] =\
    serverHeader + server_user + ':' + server_pass + '@' + server_host\
    + ':' + server_port + '/' + server_db + '?charset=' + server_charset
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True



bootstrap = Bootstrap(app)
manager = Manager(app)
moment = Moment(app)
db = SQLAlchemy(app)

def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)
manager.add_command("shell",Shell(make_context=make_shell_context))

class NameForm(Form):
    name = StringField('What is your name?',validators=[DataRequired()])
    submit = SubmitField('Submit')

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username

# db.drop_all()
# db.create_all()
# admin_role = Role(name='Admin')
# mod_role = Role(name='Moderator')
# user_role = Role(name='User')
# user_john = User(username='john',role=admin_role)
# user_susan = User(username='susan',role=user_role)
# user_david = User(username='david',role=user_role)
# db.session.add_all([admin_role,mod_role,user_role,user_john,user_susan,user_david])
# db.session.commit()

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
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        # old_name = session.get('name')
        # if old_name is not None and old_name != form.name.data:
        #     flash('Looks like you have changed your name!')
        # name = form.name.data
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html',current_time=datetime.utcnow(),form=form,name=session.get('name'),known=session.get('known', False))


@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)




if __name__ == '__main__':
    app.run(host=app.config.get('HOST',None),port=app.config.get('PORT',None))
    # manager.run()
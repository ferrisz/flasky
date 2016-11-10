#!/usr/local/python
# coding=utf-8
# Created by Ferris on 2016/11/10

from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

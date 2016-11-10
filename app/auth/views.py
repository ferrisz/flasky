#!/usr/local/python
# coding=utf-8
# Created by Ferris on 2016/11/11

from flask import render_template
from . import auth

@auth.route('/login')
def login():
    return render_template('auth/login.html')
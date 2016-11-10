#!/usr/local/python
# coding=utf-8
# Created by Ferris on 2016/11/11

from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views
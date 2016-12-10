#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/12/10

from flask import Blueprint

api = Blueprint('api', __name__)

from . import authentication, posts, users, comments, errors
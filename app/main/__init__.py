#!/usr/local/python
# coding=utf-8
# Created by Ferris on 2016/11/10

from flask import Blueprint

main = Blueprint('main', __name__)

from . import  views, errors
from ..models import Permission

@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
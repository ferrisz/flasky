#!/usr/local/python
# coding=utf-8
# Created by Ferris on 2016/11/10

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PERFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <admin@zhoufeiyu.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtpdm.aliyun.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

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

    SQLALCHEMY_DATABASE_URI = serverHeader + server_user + ':' + server_pass + '@' + server_host\
    + ':' + server_port + '/' + server_db + '?charset=' + server_charset

class TestingConfig(Config):
    TESTING = True

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

    SQLALCHEMY_DATABASE_URI = serverHeader + server_user + ':' + server_pass + '@' + server_host \
                              + ':' + server_port + '/' + server_db + '?charset=' + server_charset

class ProductionConfig(Config):
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

    SQLALCHEMY_DATABASE_URI = serverHeader + server_user + ':' + server_pass + '@' + server_host \
                              + ':' + server_port + '/' + server_db + '?charset=' + server_charset

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
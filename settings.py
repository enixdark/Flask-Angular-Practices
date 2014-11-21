# from flask import *
# import os
# from flask.ext.script import Manager,Shell
# from flask.ext.bootstrap import Bootstrap
# from flask.ext.moment import Moment
# from flask.ext.sqlalchemy import SQLAlchemy
# from flask.ext.migrate import  Migrate,MigrateCommand
# from config import *
# from flask import Blueprint
#
# main = Blueprint('main',__name__)
# from . import views,errors
#
# app.config.from_object(config['development'])
# bootstrap = Bootstrap()
# moment = Moment()
# db = SQLAlchemy()
# # migrate = Migrate(app,db)
# # manager.add_command("db",MigrateCommand)
#
# def create_app(config_name):
#     app = Flask(__name__)
#     app.config.from_object(config[config_name])
#     config[config_name].init_app(app)
#     bootstrap.init_app(app)
#     moment.init_app(app)
#     db.init_app(app)
#
#     return app
#
#
# # import ipdb;ipdb.set_trace()
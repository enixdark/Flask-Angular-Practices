from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from config import *
from flask.ext.triangle import Triangle


bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()
# migrate = Migrate(app,db)
# manager.add_command("db",MigrateCommand)
triangle = Triangle()
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    triangle.init_app(app)
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app


# import ipdb;ipdb.set_trace()
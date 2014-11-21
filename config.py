import os
basedir = os.environ.get(os.path.dirname(__file__))

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'data'
    DATABASE = os.path.join(os.getcwd(),'db.db')
    USER = 'cqshinn'
    PASSWORD = ""
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    FLASKY_ADMIN =  os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    TESTING = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + Config.DATABASE
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

class TestConfig(Config):
    TEST = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + Config.DATABASE
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

config = {
    'development':DevelopmentConfig,
    'test':TestConfig,
    'default':DevelopmentConfig
}



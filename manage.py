from app import create_app,db
from app.main import *
from flask.ext.script import Manager,Shell
from flask.ext.migrate import Migrate,MigrateCommand
import flask.ext.testing
import unittest
app = create_app('default')
manager = Manager(app)
migrage = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.command
def test():
	test = unittest.TestLoader().discover('test')
	unittest.TextTestRunner().run(test)


if __name__ == '__main__':
	manager.run()
from flask.ext.wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import *

class NameForm(Form):
    name = StringField("input your name",validators=[DataRequired()])
    submit = SubmitField("Submit")
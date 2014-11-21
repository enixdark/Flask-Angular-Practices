import datetime

from flask import request,render_template, session, redirect,url_for,flash
from . import main
from .forms import *
from ..models import *
from .. import db

@main.route('/',methods=["POST","GET"])
def home():
    return render_template('index.html',current_time=datetime.datetime.now())



@main.route('/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@main.route('/user',methods=["POST","GET"])
def user():
    form = NameForm()
    if request.method=='POST':
        if form.validate():
            session['name'] = form.name.data
            # form.name.data = ''
            return redirect(url_for('/',current_time=datetime.datetime.now()))
        else:
            flash("this field is blank")

    # if request.method == "POST":
    # 	session['user'] = request.form['username']
    return render_template('user.html',form=form)


@main.route('/test',methods=['POST','GET'])
def test():
    return render_template('test.html')


@main.route('/todo',methods=['POST','GET'])
def todo():
    return render_template('todo.html')


from urllib import request
from flask import Blueprint
from flask import Flask,render_template,flash,redirect,url_for

from app.auth.models import User
from ..auth.form import LogicForm,RegisterForm
from flask_login import login_required,current_user,login_user

auth=Blueprint('auth',__name__,template_folder='templates',static_folder='static')

@auth.route('/')
def index():
    
    
    return'<h1>home auth blueprnt her............e</h1>'

@auth.route('/login')
def login():
    form=LogicForm()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()
        login_user(user)
        next_page=request.args.get('next')
        flash(f"{ user.username } Logged successfull!", 'success')
        return redirect(next_page) if next_page else redirect(url_for('home'))
    
    return render_template('login.html',form = form)

@auth.route('/register')
def register():
    
    
    return'<h1>aregister blueprnt her............e</h1>'

@auth.route('/account')
def account():
    
    
    return'<h1>auth blueprnt her............e</h1>'

@auth.route('/logout')
def logout():
    
    
    return'<h1>auth blueprnt her............e</h1>'

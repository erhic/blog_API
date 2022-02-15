from urllib import request
from flask import Blueprint
from flask import Flask,render_template,flash,redirect,url_for
from app.auth.models import User
from ..auth.form import LogicForm,RegisterForm
from flask_login import login_required,current_user,login_user,logout_user
from werkzeug.security import generate_password_hash,check_password_hash
from ..extension import db

auth=Blueprint('auth',__name__,template_folder='templates',static_folder='static')

@auth.route('/')
def index():
    
    
    return'<h1>home auth blueprnt her............e</h1>'

@auth.route('/login',methods=['GET','POST'])
def login():
    form=LogicForm()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()
        login_user(user)
        next_page=request.args.get('next')
        flash(f"{ user.username } Logged successfull!", 'success')
        return redirect(next_page) if next_page else redirect(url_for('auth.index'))
    
    return render_template('login.html',form=form)

@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email = form.email.data,
        username = form.username.data,
         password = generate_password_hash(form.password.data))

        db.session.add(user)
        db.session.commit()
        flash('Account created successfully', 'success')

        return redirect(url_for('auth.login'))

    return render_template('login.html',form = form)
    


@auth.route('/account')
@login_required
def account():

    return render_template('account.html') 
  

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.index"))
   

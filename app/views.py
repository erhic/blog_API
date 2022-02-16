import email
from app import app,db
from .models import User
from .forms import LoginForm,RegisterForm,PostForm
from werkzeug.security import generate_password_hash,check_password_hash
from flask import render_template,redirect,url_for,flash,request,abort
from werkzeug.security import generate_password_hash,check_password_hash #used to hash password to unreadable string
from flask_login import login_required,logout_user,login_user,current_user
from app import forms
from .models import User,Post
import requests
import json



@app.route('/',methods=['GET', 'POST'])
def home():
    db.create_all()
    posts=Post.query.all()
    quote=requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    print(quote.content)
    randomquote=json.loads(quote.content)
    return  render_template('home.html',post=posts,quote=quote,data=randomquote['author'])

@app.route('/mostpopular',methods=['GET', 'POST'])
def popular():
    quote=requests.get('http://quotes.stormconsultancy.co.uk/popular.json')
    print(quote.content)
    data=json.loads(quote.content)
    return  render_template('mostpopular.html',quote=quote,data=data)


 
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            next_page = request.args.get('next') # request.args.get('next')
            flash('Logged successfull!', 'success')

            return redirect(next_page) if next_page else redirect(url_for('home'))
            
    return render_template("login.html", form=form)





@app.route('/register',methods = ["GET","POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email = form.email.data,
        username = form.username.data,
        password = generate_password_hash(form.password.data))

        db.session.add(user)
        db.session.commit()
        flash('Account created successfully', 'success')

        return redirect(url_for('login'))

    return render_template('register.html',form = form)



@app.route('/about')
def about():
    
    return  render_template('aboutus.html')



@app.route('/post',methods = ["GET","POST"])
@login_required
def post():
    form =PostForm()
    if form.validate_on_submit():
        post=Post(title=form.title.data,
                      post=form.post.data,
                      user=current_user
                      )
        db.session.add(post)
        db.session.commit()
        
        flash('Quote successfully created','sucess')
        return redirect (url_for('home'))
    return render_template ('post.html',form=form)
  

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))
   

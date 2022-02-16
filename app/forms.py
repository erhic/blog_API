# importing  the flask module that are used while creating a form
from flask_wtf import FlaskForm #the form from flask
from wtforms import StringField,BooleanField,PasswordField,SubmitField,ValidationError,TextAreaField,SelectField#the field class that we are going to use/import from the flask package wtform module module
from wtforms.validators import DataRequired,Email,EqualTo,Length,Regexp,Optional
from .models import User,Post


class RegisterForm(FlaskForm):
    '''
    class to create forms for registration and its input   
    '''
    
    # fields that are to be displayed in the register form
    
    username= StringField('Username',validators=[DataRequired(),Length(min=5,max=30,message='Provide a valid name')])
    email=StringField(' Email',validators=[DataRequired(),Email(),Length(min=5,max=30)])
    password=PasswordField('Password',validators=[DataRequired(),EqualTo('confirmpassword',message='Password required to match'),Length(min=5,max=64)])
    confirmpassword=PasswordField('Confirm Password',validators=[DataRequired()])
    submit=SubmitField('Sign Up')
    
# a function to check if a email exist to prompt user to enter another one
 
    def check_if_email_exist(self,email):
        emails= User.query.filter_by(email=email.data).first()
        if emails:
            raise ValidationError("Email already registered!")

# a function to check if a username exist to prompt user to enter another one
    def check_if_usrname_exist(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists')
      
# A form that is to filled to be authentificated or be allowed to access other webpage after/upon/to registering 
class LoginForm(FlaskForm):
    '''
    class to create forms for login and its input   
    '''
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Enter your Password',validators=[DataRequired()])
    remember_me=BooleanField('Remember Me',validators=[Optional()])
    submit=SubmitField('Login')
    
    
class UpdateForm(FlaskForm):
    '''
    class to update forms   
    '''
    username= StringField('Username',validators=[DataRequired(),Length(min=3,max=30,message='Provide a valid name'),Regexp('A-Za-z',message='Your name must contain letters only')])
    email=StringField(' Email',validators=[DataRequired(),Email(),Length(min=5,max=30)])
    password=PasswordField('Password',validators=[DataRequired(),EqualTo('confirmpassword',message='Password required to match'),Length(min=5,max=64)])
    submit=SubmitField('Update')
    
class PostForm(FlaskForm):
    '''
    class to create quotes   
    '''
    title = StringField('Quote Title',validators=[DataRequired()])
    post= TextAreaField('Quote',validators=[DataRequired()])
    submit = SubmitField('Post')
    
    
    
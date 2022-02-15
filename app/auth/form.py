from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length,EqualTo,ValidationError
from ..auth.models import User,UserMixin,user_loader


class RegisterForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired()])
    email=StringField('Email',validators=[DataRequired(),Length(min=4,max=15)])
    password=PasswordField('Password',validators=[DataRequired(),Length(min=5,max=12)])
    confirmpassword=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Register')
    
    
class LogicForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired(),Length(min=5,max=12)])
    submit=SubmitField('Register')
    
# valiadating username
    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Userame already exist')
        
# validating email
    def validate_email(self,email):
        emailaddr=User.query.filter_by(email=email.data).first()
        if emailaddr:
            raise ValidationError('Email already exist')
            
        

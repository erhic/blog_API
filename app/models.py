# imported classes# imported classes
from app import db
from app import login_manager
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# our user database table model/architecture
class User(db.Model,UserMixin):
    __tablename__='user' #name of the table in the db
    
    # columns in Our User db table
    id= db.Column(db.Integer,primary_key = True)
    username=db.Column(db.String(50),unique = True)
    email=db.Column(db.String(150),unique = True)
    password=db.Column(db.String(150))
    post= db.relationship('Post', backref='user', lazy=True)
                             
                             
class Post(db.Model):
    __tablename__= 'post'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(200))
    # category = db.Column(db.String(200))
    post = db.Column(db.String(400))
    datetime = db.Column(db.DateTime(200), default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    

    
    
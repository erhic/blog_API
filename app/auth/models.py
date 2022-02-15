from extension import db
from flask_login import login_manager,UserMixin
from loginconfig import login_manager
from ..quotes.model import Quotes

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)


class User(db.Model,UserMixin):
    __tablename__='user'
    
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50),nullable=False,unique=True)
    email=db.Column(db.String(50),nullable=True,unique=True)
    password=db.Column(db.String(70),nullable=True)
    quotes=db.relationship('Quotes',backref='user',lazy=True)


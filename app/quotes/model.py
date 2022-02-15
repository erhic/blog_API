from turtle import title
from unicodedata import category
from extension import db
from datetime import datetime
from ..auth.models import User,UserMixin,user_loader
 
class Quotes(db.Model):
    __tablename__='quotes'
    
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(30),nullable=False)
    category=db.Column(db.String(),nullable=False)
    content=db.Column(db.String(nullable=False))
    time=db.Column(db.String(nullable=False))
    post_user = db.Column(db.Integer, db.ForeignKey('user.id'))

    
    
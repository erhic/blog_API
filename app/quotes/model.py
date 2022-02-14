from turtle import title
from unicodedata import category
from extension import db

class Quotes(db.Model):
    __tablename__='quotes'
    
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(30),nullable=False)
    category=db.Column()
    content=db.Column()
    time=db.Column()
    
    
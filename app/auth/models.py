from extension import db

class User(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    username=db.Column(db.String(50),nullable=False,unique=True)
    email=db.Column(db.String(50),nullable=True,unique=True)
    password=db.Column(db.String(70),nullable=True)
    


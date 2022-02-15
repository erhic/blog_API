from ..extension import db
from datetime import datetime
# from ..auth.models import User
 
class Quotes(db.Model):
    __tablename__='quotes'
    
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(30),nullable=False)
    category=db.Column(db.String(200),nullable=False)
    content=db.Column(db.String(200),nullable=False)
    time=db.Column(db.DateTime,nullable=False, default = datetime.utcnow)
    post_user = db.Column(db.Integer, db.ForeignKey('user.id'))

    
    
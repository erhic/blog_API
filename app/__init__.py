from flask import Flask,Blueprint
from auth import auth
from quotes import quotes

def create_app():
    app=Flask(__name__)
    
    app.register_blueprint(auth)
    app.register_blueprint(quotes)
    
    return app
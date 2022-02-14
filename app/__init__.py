from flask import Flask,Blueprint
from auth import auth
from quotes import quotes

def create_app(config_file='settings.py'):
    app=Flask(__name__)
    app.config.from_pyfile(config_file)
    app.register_blueprint(auth)
    app.register_blueprint(quotes)
    
    return app
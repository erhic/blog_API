from flask import Flask,Blueprint
from .auth import auth
from .quotes import quotes
from .extension import db
from .loginconfig import login_manager

def create_app(config_file='settings.py'):
    app=Flask(__name__)
    app.config.from_pyfile(config_file)
    
     # login intialization
    login_manager.init_app(app)

    # db intialization
    db.init_app(app)
    
    
    app.register_blueprint(auth,url_prefix='/auth')
    app.register_blueprint(quotes,url_prefix='/quotes')
    
    return app
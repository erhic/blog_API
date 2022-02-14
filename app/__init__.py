from flask import Flask,Blueprint
from .auth import auth
from .quotes import quotes
from .extension import db
from flask_login import LoginManager

def create_app(config_file='settings.py'):
    app=Flask(__name__)
    app.config.from_pyfile(config_file)
    
    # login configuration
    login_manager=LoginManager()
    login_manager.init_app(app)
    login_manager.login_view='login'
    login_manager.login_message_category='Success'
    
    db.init_app(app)
    app.register_blueprint(auth,url_prefix='/auth')
    app.register_blueprint(quotes,url_prefix='/quotes')
    
    return app
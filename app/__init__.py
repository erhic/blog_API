from flask import Flask
from .config import ProdConfig
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate

app = Flask(__name__)

login_manager = LoginManager(app)
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'

# Creating the app configurations
app.config.from_object(ProdConfig)


db = SQLAlchemy(app)
mail = Mail(app)
Migrate(app,db)

# app.config[''] = False
from app import views
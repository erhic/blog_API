from flask_login import LoginManager

# login configuration
login_manager=LoginManager()
login_manager.login_view='login'
login_manager.login_message_category='Success'
from flask import Blueprint
from flask import Flask,render_template

auth=Blueprint('auth',__name__,template_folder='templates',static_folder='static')

@auth.route('/')
def main_index():
    
    
    return'<h1>auth blueprnt her............e</h1>'

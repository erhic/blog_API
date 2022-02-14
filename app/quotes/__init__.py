from flask import Blueprint
from flask import Flask,render_template


quotes=Blueprint('quotes',__name__,template_folder='templates',static_folder='static')



@quotes.route('/quotes')
def main_index():
    return 'blueprint for qoutes'

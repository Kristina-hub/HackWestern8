from flask import Flask, render_template, request, url_for, redirect
from bs4 import BeautifulSoup
import requests
application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/query')
def query():
   return render_template('query.html')

@application.route('/query', methods=['POST'])
def my_form_post():
    text = request.form['text']
    query = text.upper()
    
    # string = function(query)
    # input string into stocks.html
    
    # graph = function(query)
    # input graph into stocks.html
    
    return query

@application.route('/stocks', methods=['GET', 'POST'])
def stocks():
   return render_template('stocks.html')
   
'''
To test locally:
export FLASK_APP="application.py"
flask run
command shift R to reload static files
'''
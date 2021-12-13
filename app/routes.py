from app import app
from flask import render_template

from flask_login import login_required


# This is called a view funciton, which are 
# the different URLS the application implements.

@app.route('/')
@app.route('/index')
def homepage():
    return render_template('index.html', my_title = "This is the HOME page", name='Shoha')

@app.route('/about')
@login_required
def iCanNameThisAnything():
    return render_template('about.html', my_title = "aBoUt")

@app.route('/testing')
def test():
    return {'hi':'there'}
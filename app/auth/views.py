from flask import render_template
from app.auth import auth

@auth.route('/login')
def login():
    return render_template('login.html', text='Testing')

@auth.route('/signup')
def signup():
    return render_template('sign_up.html', text='Testing')
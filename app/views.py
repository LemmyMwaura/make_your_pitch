from flask import render_template
from app import app

@app.route('/')
@app.route('/home')
def home():
    return '<h1>home</h1>'

@app.route('/login')
def login():
    return '<h1>login</h1>'

@app.route('/signup')
def signup():
    return '<h1>sign up</h1>'

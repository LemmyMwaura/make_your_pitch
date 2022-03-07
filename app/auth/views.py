from flask import render_template,redirect,url_for,request,flash
from app.auth import auth
from app import db
from app.models import User

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', text='Testing')

@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    firstname = request.form.get('fname')
    lastname = request.form.get('lname')
    email = request.form.get('email')
    username = request.form.get('uname')
    password = request.form.get('pass')
    confirm_password = request.form.get('cpass')

    email_exists = User.query.filter_by(email=email).first()
    username_exists = User.query.filter_by(username=username).first()
    if email_exists:
        flash('Email is already in use', category='error')
    elif username_exists:
        flash('Username is alredy in use', category='error')
    elif password != confirm_password:
        flash('Passwords don\'t match', category='error')
    elif len(username) < 2:
        flash('Username is too short', category='error')
    elif len(password) < 8:
        flash('Password is too short', category='error')
    elif len(email) < 4:
        flash('Email is invalid', category='error')
    else:
        new_user= User(
            firstname=firstname,
            lastname=lastname,
            email=email,
            username=username,
            password=password
        )
        db.session.add(new_user)
        db.session.commit()
        flash('User created')
        return redirect(url_for('views.login'))

    return render_template('sign_up.html', message='You have already submitted feedback')

@auth.route('/logout')
def logout():
    return redirect(url_for('home'))

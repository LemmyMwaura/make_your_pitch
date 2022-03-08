from flask import render_template,redirect,url_for,request,flash
from app.auth import auth
from app import db
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_user, logout_user, login_required

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if user:= User.query.filter_by(email=email).first():
            if check_password_hash(user.password, password):
                flash("Logged in!", category='success')
                login_user(user, remember=True)
                return redirect(url_for('view.home'))
            else:
                flash('Password is incorrect.', category='error')
        else:
            flash('Email does not exist', category='error')

    return render_template('login.html', text='Testing', user=current_user)

@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
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
                password=generate_password_hash(password, method='sha256')
            )
            db.session.add(new_user)
            db.session.commit()
            flash('User created')
            login_user(new_user, remember=True)
            return redirect(url_for('view.home'))

    return render_template('sign_up.html', message='You have already submitted feedback', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('view.home'))

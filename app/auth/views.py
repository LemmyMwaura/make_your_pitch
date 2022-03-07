from app.auth import auth

@auth.route('/login')
def login():
    return '<h1>login</h1>'

@auth.route('/signup')
def signup():
    return '<h1>sign up</h1>'

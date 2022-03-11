from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
import re

db = SQLAlchemy()
migrate = Migrate()
DB_USER='postgres'
DB_PASS='adminlemmy'
ENV='Prod'

def create_database(app):
    with app.app_context():
        db.create_all()

def create_app():
    app = Flask(__name__)

    from .views import view, cat, post
    from .auth import auth
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(view, url_prefix='/')
    app.register_blueprint(post, url_prefix='/posts')
    app.register_blueprint(cat, url_prefix='/posts/category')

    if ENV =='dev':
        app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@localhost/pitchesapp'
        create_database(app)
    else:
        URI = os.environ.get('DATABASE_URL')
        if URI.startswith('postgres://'):
            URI= URI.replace('postgres://', 'postgresql://', 1)
        app.config['SQLALCHEMY_DATABASE_URI'] = URI

    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app,db)
    

    from .models import User
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


from app import views
from app import errors


from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()
DB_USER='postgres'
DB_PASS='adminlemmy'

def create_app():
    app = Flask(__name__)

    from .views import view
    from .auth import auth
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(view, url_prefix='/')

    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@localhost/pitchesapp'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    return app

from app import views
from app import errors


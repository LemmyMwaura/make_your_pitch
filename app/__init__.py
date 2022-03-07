from flask import Flask
from app.auth import auth

app = Flask(__name__)
app.register_blueprint(auth, url_prefix='/auth')

from app import views
from app import errors


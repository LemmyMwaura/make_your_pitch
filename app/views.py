from flask import render_template, Blueprint
from flask_login import current_user,login_required

view = Blueprint('view',__name__)

@view.route('/')
@view.route('/home')
def home():
    return render_template('index.html', user=current_user)

from urllib.request import CacheFTPHandler
from app import db
from app.models import Category
from flask import render_template, Blueprint
from flask_login import current_user,login_required

view = Blueprint('view',__name__)

@view.route('/')
@view.route('/home')
def home():
    categories = ['Buiness/Ecommerce','Tech','Games','Fashion','Science','Crypto/Web3']
    for category in categories:
        if cate_exists := Category.query.filter_by(name=category).first():
            print('Already exists')
        else:
            new_category = Category(category)
            db.session.add(new_category)
            db.session.commit()

    all_categories = Category.query.order_by(Category.id)
    return render_template('index.html', user=current_user, categories=all_categories)

@view.route('/all_posts')
def posts():

    return render_template('posts.html', user=current_user)
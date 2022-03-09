from app import db
from app.models import Category, Posts
from flask import render_template, Blueprint, flash
from flask_login import current_user,login_required

view = Blueprint('view',__name__)
cat = Blueprint('cat',__name__)

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

@view.route('/posts')
def posts():
    all_posts = Posts.query.order_by(Posts.date_posted)
    return render_template('posts.html', user=current_user, posts=all_posts)

@view.route('/posts/delete/<int:id>')
@login_required
def delete_post(id):
    post_to_delete = Posts.query.get_or_404(id)
    try:
        if current_user.id != post_to_delete.id:
            flash('You do not have permission to delete this post.(Not the author)')
        else:
            db.session.delete(post_to_delete)
            db.session.commit()
            flash("Blog post was deleted", category='success')
    except:
        flash('Woops there was a problem deleting post. Try again', category='danger')

    all_posts = Posts.query.order_by(Posts.date_posted)
    return render_template('posts.html', user=current_user, posts=all_posts)

@cat.route('/Business')
def bsns():
    bsns_posts = Posts.query.filter_by(category_id=1)
    return render_template('category.html', user=current_user, posts=bsns_posts)

@cat.route('/Technology')
def tech():
    tech_posts = Posts.query.filter_by(category_id=2)
    return render_template('category.html', user=current_user, posts=tech_posts)

@cat.route('/Gaming')
def games():
    games_posts = Posts.query.filter_by(category_id=3)
    return render_template('category.html', user=current_user, posts=games_posts)

@cat.route('/Fashion')
def fashion():
    fashion_posts = Posts.query.filter_by(category_id=4)
    return render_template('category.html', user=current_user, posts=fashion_posts)

@cat.route('/Science')
def science():
    science_posts = Posts.query.filter_by(category_id=5)
    return render_template('category.html', user=current_user, posts=science_posts)

@cat.route('/Crypto-web3')
def crypto():
    web3_posts = Posts.query.filter_by(category_id=6)
    return render_template('category.html', user=current_user, posts=web3_posts)


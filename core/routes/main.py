from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

from ..models import User

main = Blueprint('main', __name__)

@main.route('/')
def index():

    context={
        'title': 'Brotherhood Records | Home'
    }

    return render_template(
        'index.html',
        **context
    )

@main.route('/products')
def get_products():

    context={
        'title': 'Products | Home'
    }

    return render_template(
        'products.html',
        **context
    )



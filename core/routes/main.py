from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

from ..models import User

main = Blueprint('main', __name__)

@main.route('/')
def index():

    return redirect(url_for('product.get_products'))

@main.route('/success/')
def success():
    context = {
        'title': 'Order purchased successfully',
    }

    return render_template(
        'success.html',
        **context
    )
@main.route('/cancelled/')
def cancel():
    context = {
        'title': 'Order Cancelled',
    }

    return render_template(
        'cancel.html',
        **context
    )





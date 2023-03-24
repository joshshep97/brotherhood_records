from ..models import Product

from flask import Blueprint, render_template, request, redirect

import stripe
import os
from flask_login import current_user

product = Blueprint('product', __name__)

@product.route('/')
def get_products():
    sort = request.args.get('sort')

    context={
        'title': 'Products | Home',
        'products': Product.query
        .order_by(sort)
        .all(),
    }

    return render_template(
        'products.html',
        **context
    )

@product.route('/<int:id>/')
def product_page(id):
    selected_product = Product.query.filter_by(
        id=id
    ).first()

    context = {
        'title': selected_product.title,
        'product': selected_product,
    }

    return render_template(
        'product_page.html',
        **context
    )

@product.route('/genre/<genre>/')
def product_by_genre(genre):
    sort = request.args.get('sort')

    context={
        'title': 'Products | Home',
        'products': Product.query
        .filter_by(genre=genre)
        .order_by(sort)
        .all(),
    }

    return render_template(
        'products.html',
        **context
    )

@product.route('/artist/<artist>/')
def get_artist(artist):
    artist_products = Product.query.filter_by(artist=artist).all()
    context = {
        'title': f'Products | {Product.artist}',
        'products': artist_products,
    } 
    return render_template(
        'products.html',
        **context
    )


DOMAIN = 'http://127.0.0.1:5000'

stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')

@product.route('/<int:id>/create-checkout-session/', methods=['GET', 'POST'])
def create_checkout_session(id):
    product = Product.query.filter_by(id=id).first()
    price_id = product.price_id

    try:
        checkout_session = stripe.checkout.Session.create(
            customer_email = current_user.email,
            submit_type='pay',
            billing_address_collection='auto',
            shipping_address_collection={
            'allowed_countries': ['GB']
            },
            line_items=[
                {
                'price': price_id,
                'quantity': 1,
                },
            ],
            mode='payment',
            success_url=DOMAIN + '/success',
            cancel_url=DOMAIN + '/cancelled',
        )
    except Exception as e:
        return str(e)

    return redirect(
        checkout_session.url,
        code=303
    )


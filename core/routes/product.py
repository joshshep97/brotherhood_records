from ..models import Product
from .. import db

from flask import Blueprint, render_template, request, redirect, url_for, flash

import stripe
import os
from flask_login import current_user, login_required


product = Blueprint('product', __name__)


def get_genres():
    genres = set()
    for product in Product.query.all():
        genres.add(product.genre)
    return list(genres)

@product.route('/')
def get_products():
    sort = request.args.get('sort')

    context={
        'title': 'Products | Home',
        'products': Product.query
        .order_by(sort)
        .all(),
        'genres': get_genres(),
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
        'genres': get_genres(),
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
        'genres': get_genres(),
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
        'genres': get_genres(),
    } 
    return render_template(
        'products.html',
        **context
    )

@product.route('add-to-collection/<int:id>/')

@login_required
def add_to_collection(id):
    product = Product.query.filter_by(id=id).first()
    if product in current_user.collection:
        flash('You have already added this to your collection', 'error')
        return redirect(url_for('profile.get_profile', id=current_user.id))
    else:
        current_user.collection.append(product)
        db.session.commit()
        flash('Product added to your collection','success')
        return redirect(url_for('profile.get_profile', id=current_user.id))

@product.route('/remove-from-collection/<int:id>/')

@login_required
def remove_from_collection(id):
    product = Product.query.filter_by(id=id).first()
    if product not in current_user.collection:
        flash('You have not added this to your collection', 'error')
        return redirect(url_for('profile.get_profile', id=current_user.id))
    else:
        current_user.collection.remove(product)
        db.session.commit()
        flash('Product removed from your collection','success')
        return redirect(url_for('profile.get_profile', id=current_user.id))
    
DOMAIN = 'http://127.0.0.1:5000'

stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')


@product.route('/<int:id>/create-checkout-session/', methods=['GET', 'POST'])
@login_required
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
            success_url=f'{DOMAIN}/products/add-to-collection/{str(product.id)}',
            cancel_url=DOMAIN + '/cancelled',
        )
    except Exception as e:
        return str(e)
    flash('Purchase Successful!', 'success')

    return redirect(
        checkout_session.url,
        code=303
    )


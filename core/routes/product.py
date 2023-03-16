from ..models.product import Product

from flask import Blueprint, render_template, request, redirect
import stripe
import os

product = Blueprint('product', __name__)



@product.route('/')
def get_products():
    products = Product.query.all()

    context={
        'title': 'Products | Home',
        'products': products
    }

    return render_template(
        'products.html',
        **context
    )

@product.route('/<int:id>')
def product_page(id):
    selected_product = Product.query.filter_by(id=id).first()

    context = {
        'title': selected_product.title,
        'product': selected_product,
    }

    return render_template(
        'product_page.html',
        **context
    )

DOMAIN = 'http://127.0.0.1:5000'

stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')

@product.route('/create-checkout-session/<int:id>/', methods=['GET', 'POST'])
def create_checkout_session(id):
    product = Product.query.filter_by(id=id).first()
    price_id = product.price_id

    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                'price': price_id,
                'quantity': 1,
                },
            ],
            mode='payment',
            success_url=DOMAIN + '/success.html',
            cancel_url=DOMAIN + '/cancel.html',
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)

# to do 
# - add routes & templates for success and cancel
# - edit S+C urls for URL_FOR
# - add products on stripe dashboard
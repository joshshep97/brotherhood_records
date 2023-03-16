from flask import Blueprint
import stripe
import os

payments = Blueprint('payments', __name__)

DOMAIN = 'http://127.0.0.1:5000'

stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')

@payments.route('/create-checkout-session/', methods=['GET', 'POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
            'price':
            ]
        )
    except Exception as e:
        return str(e)
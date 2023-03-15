from ..models.product import Product

from flask import Blueprint, render_template, request

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


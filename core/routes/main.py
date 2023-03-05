from flask import Blueprint, render_template

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
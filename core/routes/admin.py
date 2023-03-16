from flask import Blueprint, render_template, request, url_for, redirect, flash
from flask_login import current_user, login_required

from ..models import Product
from ..datebase import db

admin = Blueprint('admin', __name__)

@login_required
@admin.route('/')
def index():
    if current_user.is_authenticated and current_user.is_admin == True:

        context = {
            'title': 'Admin | Home',
            'records': Product.query.all()
        }

        return render_template(
            'admin/index.html',
            **context
        )
    else:
        return '<h1>You are not authorized</h1>'

@login_required
@admin.route('/add_record/', methods=['GET', 'POST'])
def add_record():
    if current_user.is_authenticated and current_user.is_admin == True:
        if request.method == 'POST':
            title = request.form.get('title').title()
            artist = request.form.get('artist').title()
            genre = request.form.get('genre').title()
            price = float(request.form.get('price'))
            price_id = request.form.get('price_id')
            release_year = int(request.form.get('release_year'))
            image_url = request.form.get('image_url')

            record = Product(
                title = title,
                artist = artist,
                genre = genre,
                price = price,
                price_id = price_id,
                release_year = release_year,
                img_url = image_url
            )

            db.session.add(record)
            db.session.commit()
            flash('New record created', 'success')

            return redirect(url_for('admin.index'))
    else:
        flash('You are not authorized to view this page.', 'error')
        return redirect(url_for('main.index'))

    context = {
        'title': 'Add Record'
    }

    return render_template(
        'admin/add_record.html',
        **context
    )

@admin.route('/edit_record/<int:id>/')
def edit_record(id):
    selected_record = Product.query.filter_by(id=id).first()

    context = {
        'title': 'Edit Record',
        'record': selected_record
    }

    return render_template(
        'admin/edit_record.html',
        **context
    )
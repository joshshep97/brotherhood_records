from flask import Blueprint, url_for, render_template, redirect, request, flash
from flask_login import current_user, login_required

from ..models import User
from ..datebase import db

profile = Blueprint('profile', __name__)


@login_required
@profile.route('/<int:id>/')
def get_profile(id):

    selected_user = User.query.filter_by(id=id).first()
    
    context = {
        'title': 'Your Profile',
        'user': current_user,
        'selected_user': selected_user
    }

    if current_user.is_authenticated:
        return render_template(
            'user_profile.html',
            **context
        )
    else:
        flash('You must be loggin in to view this page', 'error')
        return redirect(url_for('main.index'))
    

@login_required
@profile.route('/<int:id>/edit_name', methods=['GET', 'POST'])
def edit_name(id):
    selected_user = User.query.filter_by(id=id).first()

    if request.method == 'POST':
        selected_user.name = request.form.get('name')
        db.session.commit()
        flash('Name Changed Successfully')

        return redirect(url_for('profile.get_profile', id = current_user.id))
    
    context = {
        'title': 'Edit Name',
        'user': current_user,
        'selected_user': selected_user,
        'attribute': 'name',
    }

    return render_template(
        'edit_profile.html',
        **context
    )

@login_required
@profile.route('/<int:id>/edit_email', methods=['GET', 'POST'])
def edit_email(id):
    selected_user = User.query.filter_by(id=id).first()

    if request.method == 'POST':
        selected_user.email = request.form.get('email')
        db.session.commit()
        flash('Email Changed Successfully')

        return redirect(url_for('profile.get_profile', id = current_user.id))
    
    context = {
        'title': 'Edit Email',
        'user': current_user,
        'selected_user': selected_user,
        'attribute': 'email',
    }

    return render_template(
        'edit_profile.html',
        **context
    )

# TO DO:
# EDIT USERNAME
# ADD FAVORITE GENRES
# CHANGE PASSWORD
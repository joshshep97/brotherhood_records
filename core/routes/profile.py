from flask import (
    Blueprint, 
    url_for, 
    render_template, 
    redirect, 
    request, 
    flash
)

from flask_login import current_user, login_required
from werkzeug.security import (check_password_hash, 
                               generate_password_hash)

from ..models import User, FavoriteGenre
from ..datebase import db
from .product import get_genres
import re

profile = Blueprint('profile', __name__)


@profile.route('/<int:id>/', methods=['GET', 'POST'])
@login_required
def get_profile(id):
    if request.method == 'POST':
        genre = request.form.get('genre').title( )

        f_genre = FavoriteGenre(name=genre, 
                                user=current_user)

        genre_exists = bool(FavoriteGenre.query.filter_by(
            user=current_user, 
            name=f_genre.name
        ).first())
        
        if genre_exists:
            flash('You have already added this genre', 'error')
        else:
            db.session.add(f_genre)
            db.session.commit()
            flash('Genre Added Successfully', 'success')

    if id != current_user.id:
        return redirect(url_for('profile.get_profile', 
                                id=current_user.id))
    else:
        context = {
            'title': 'Your Profile',
            'user': current_user,
            'genres': current_user.favorite_genres,
            'product_genres': get_genres()
        }

        if current_user.is_authenticated:
            return render_template(
                'user_profile.html',
                **context
            )
        else:
            flash(
                'You must be loggin in to view this page', 
                'error'
            )
            return redirect(url_for('main.index'))
    

@profile.route('/<int:id>/edit_name/', 
               methods=['GET', 'POST'])
@login_required
def edit_name(id):
    selected_user = User.query.filter_by(
        id=id
    ).first()

    if request.method == 'POST':
        selected_user.name = request.form.get('name')
        db.session.commit()
        flash('Name Changed Successfully')

        return redirect(url_for('profile.get_profile', 
                                id = current_user.id))
    
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

@profile.route('/<int:id>/edit_email/', 
               methods=['GET', 'POST'])
@login_required
def edit_email(id):
    selected_user = User.query.filter_by(
        id=id
    ).first()

    if request.method == 'POST':
        selected_user.email = request.form.get('email')
        db.session.commit()
        flash('Email Changed Successfully')

        return redirect(url_for('profile.get_profile', 
                                id = current_user.id))
    
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

@profile.route('/<int:id>/edit_username/', 
               methods=['GET', 'POST'])
@login_required
def edit_username(id):
    if id != current_user.id:
        return redirect(
            url_for('profile.edit_username', 
                    id=current_user.id)
        )
    else:
        if request.method == 'POST':
            current_user.username = request.form.get(
                'username'
            )
            db.session.commit()
            flash('Username Changed Successfully')

            return redirect(
                url_for('profile.get_profile', 
                        id = current_user.id)
            )
        
        context = {
            'title': 'Edit Username',
            'user': current_user,
            'selected_user': current_user,
            'attribute': 'username',
        }

        return render_template(
            'edit_profile.html',
            **context
        )

@profile.route(
    '/<int:id>/change_password/',
    methods=['GET', 'POST']
)
@login_required
def change_password(id):
    if id != current_user.id:
        return redirect(url_for(
            'profile.change_password',
            id=current_user.id
        ))
    else:
        if request.method == 'POST':
            current_password = request.form.get('current_password')
            new_password = request.form.get('new_password')

            if not check_password_hash(
                current_user.password, 
                current_password
            ):
                flash('Password is incorrect', 'error')
            else:
                password_is_valid = False
                if re.search('[A-Z]', new_password) is None:
                    password_is_valid = False
                    flash(
                        'Password must contain at least one uppercase',
                        'error'
                    )
                elif re.search('[0-9]', new_password) is None:
                    password_is_valid = False
                    flash(
                        'Password must include at least one numbber', 
                        'error'
                    )
                elif re.search('["£$@#~!?"]', new_password) is None:
                    password_is_valid = False 
                    flash(
                        '''Password must include one of the following 
                        special characters: £ $ @ # ~ ! ?
                        ''', 
                        'error'
                    )
                else:
                    password_is_valid = True

                if password_is_valid:
                    current_user.password = generate_password_hash(
                        new_password,
                        method='sha256'
                    )
                    db.session.commit()
                    flash('Password Changeed', 'success')

                return redirect(
                    url_for(
                    'profile.get_profile',
                    id=current_user.id
                    )
                )

        context = {
            'title': 'Change Password'
        }
        return render_template(
            'change_password.html',
            **context
        )
    

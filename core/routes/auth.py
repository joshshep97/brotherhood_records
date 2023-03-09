import re

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from ..models import User
from .. import db

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in', 'success')
                login_user(user, remember=True)
                return redirect(url_for('main.index'))
            else:
                flash('Password is incorrect', 'error')
        else: 
            flash('User does not exist', 'error')

    return render_template(
        'login.html',
        title='Login',
        user = current_user
    )

@auth.route('/register', methods=['GET', 'POST'])
def register():
    # TODO:
    # ADD EMAIL CONFIRMATION

    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        password_confirmation = request.form.get('password_confirmation')

        is_validated = False
        username_exists = bool(User.query.filter_by(username = username).first())
        email_exists = bool(User.query.filter_by(email = email).first())

        # username validation
        if username == '':
            is_validated = False
            flash('Username must be provided', 'error')
        elif username_exists:
            is_validated = False
            flash('Username must be unique', 'error')
        # email validation
        elif email_exists:
            is_validated = False
            flash('Email in use. If you already have an account, please login', 'error')
        elif len(email) < 5:
            is_validated = False
            flash('Please enter a valid email address', 'error')
        # password validation
        elif re.search('[A-Z]', password) is None:
            is_validated = False
            flash('Password must contain at least one uppercase', 'error')
        elif re.search('[0-9]', password) is None:
            is_validated = False
            flash('Password must include at least one numbber', 'error')
        elif password != password_confirmation:
            is_validated = False
            flash('passwords must match', 'error')
        else:
            is_validated = True
        
        if is_validated:
            usr = User(
                username = username,
                email = email,
                password = generate_password_hash(password, method='sha256')
            )

            db.session.add(usr)
            db.session.commit()
            flash('Account Created Successfully', 'success')
            return redirect(url_for('auth.login'))
    
    context={
        'title': 'Register | Brotherhood Records',
    }

    return render_template(
        'register.html',
        **context
    )

@auth.route('/logout')
def logout():
    logout_user()
    flash('Logged out successfully', 'success')
    return redirect(url_for('main.index'))
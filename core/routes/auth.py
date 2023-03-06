from flask import Blueprint, render_template, request, flash
from ..models import User
from .. import db
from werkzeug.security import generate_password_hash

auth = Blueprint('auth', __name__)





@auth.route('/login')
def login():
    
    context={
        'title': 'Login | Brotherhood Records',
    }

    return render_template(
        'login.html',
        **context
    )

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        password_confirmation = request.form.get('password_confirmation')

        is_validated = False

        if username and password == '':
            is_validated = False
        elif username == User.query.filter_by(username=User.username).first():
            is_validated = False
        elif email == User.query.filter_by(email=User.email).first():
            is_validated = False
        elif len(email) < 5:
            is_validated = False
        elif password != password_confirmation:
            is_validated = False
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
        else:
            return 'Not Valid'
    
    context={
        'title': 'Register | Brotherhood Records',
    }

    return render_template(
        'register.html',
        **context
    )
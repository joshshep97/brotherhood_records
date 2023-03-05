from flask import Blueprint, render_template

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

@auth.route('/register')
def register():
    
    context={
        'title': 'Register | Brotherhood Records',
    }

    return render_template(
        'register.html',
        **context
    )
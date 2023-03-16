from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from werkzeug.security import generate_password_hash

from dotenv import load_dotenv

from os import path
import os

from .datebase import db
from .models import User


login_manager = LoginManager()
DB_NAME = 'database.db'


def create_app():

    load_dotenv()

    app = Flask(__name__)
    # app configuration
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URL')
    db.init_app(app)

    @app.route('/test')
    def test():
        return 'success'
    
    # register blueprints

    from .routes import api as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from .routes import main as main_bp
    app.register_blueprint(main_bp, url_prefix='/')

    from .routes import auth as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    
    from .routes import profile as profile_bp
    app.register_blueprint(profile_bp, url_prefix='/profile')

    from .routes import product as product_bp
    app.register_blueprint(product_bp, url_prefix='/products')

    from .routes import admin as admin_bp
    app.register_blueprint(admin_bp, url_prefix='/admin')

    # if no database in filesystem, one will be created
    create_database(app)

    app.app_context().push()

    # if admin account doesn't exist, one will be created
    admin_exists = bool(User.query.filter_by(
        username = 'admin'
    ).first())
    if not admin_exists:
        admin = User(
                    username = os.environ.get('admin_username'),
                    email = os.environ.get('admin_email'),
                    password = generate_password_hash(os.environ.get('admin_password'), method='sha256'),
                    is_admin = True,
                    name = 'Admin'
                )

        db.session.add(admin)
        db.session.commit()

    # Create flask login instance
    login_manager.init_app(app)
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    login_manager.login_view = 'auth.login'


    return app

def create_database(app):
    if not path.exists('core/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Database created successfully')
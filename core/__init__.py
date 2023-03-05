from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path


db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'helloworld'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    @app.route('/test')
    def test():
        return 'success'

    from .routes.main import main as main_bp
    app.register_blueprint(main_bp, url_prefix='/')

    create_database(app)

    return app

def create_database(app):
    if not path.exists('core/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Database created successfully')
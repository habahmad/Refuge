from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from os import path
from flask import current_app

db = SQLAlchemy()
DB_NAME = "database.db"  #db object used to interact with database


def create_app():
    app = Flask(__name__)
    #encrypt cookies and session data 
    app.config['SECRET_KEY'] = 'encryption key'

    #storing database in website folder
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    #initialize db
    db.init_app(app)

    #registering blueprints 
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import user_comments, happy_response, sad_response, content_response
    create_database(app)

    return app

def create_database(app):
    with app.app_context():
        if not path.exists('website/' + DB_NAME): 
            db.create_all()
            print('Created database!')
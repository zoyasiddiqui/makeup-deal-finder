from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager, login_manager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET KEY'] = "secret key"
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///database.db'
    db.init_app(app)

    with app.app_context():
        db.create_all()

    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    return app
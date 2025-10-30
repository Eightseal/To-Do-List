import os

from flask import Flask

from .config import Config
from .extensions import db, migrate
from .routes.index.index import index_bp
from .routes.list.list_item import list_bp
from .routes.users.users import users_bp


def create_app(app_config=Config):
    app = Flask(__name__)
    app.config.from_object(app_config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    app.register_blueprint(index_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(list_bp)

    return app

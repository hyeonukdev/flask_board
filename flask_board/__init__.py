"""Initialize Flask app."""
import os
from flask import Flask
from flask_assets import Environment
from flask_sqlalchemy import SQLAlchemy


def init_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my.sqlite3'
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'flask board'

    db = SQLAlchemy(app)

    assets = Environment()
    assets.init_app(app)
    with app.app_context():
        db.create_all()
        # Import parts of our application
        from .assets import compile_static_assets
        from .home import home
        from .about import about
        from .profile import profile
        from .qna import qna

        # Register Blueprints
        app.register_blueprint(home.home_bp)
        app.register_blueprint(about.about_bp)
        app.register_blueprint(profile.profile_bp)
        app.register_blueprint(qna.qna_bp)

        # Compile static assets
        compile_static_assets(assets)

        return app
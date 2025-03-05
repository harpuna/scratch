from flask import Flask
from extensions import api, db, ma, migrate


def create_app() -> Flask:
    app = Flask("scratch")
    app.config.from_object("config.Config")
    configure_extensions(app)
    register_blueprints(api)
    return app

def configure_extensions(app: Flask) -> None:
    """configure flask extensions"""
    db.init_app(app)
    ma.init_app(app)
    api.init_app(app)
    migrate.init_app(app, db)

def register_blueprints(api) -> None:
    from routes.web_routes import web_bp
    from routes.customer import customer_bp
    from routes.test import test_bp

    api.register_blueprint(web_bp, url_prefix="/web")  # Web pages
    api.register_blueprint(customer_bp)
    api.register_blueprint(test_bp)


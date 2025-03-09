from config import app_config
from extensions import api, db, ma, migrate
from flask import Flask


def create_app(config_class=app_config) -> Flask:
    app = Flask("scratch")
    app.config.from_object(config_class)
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
    from routes.customer import customer_bp
    from routes.health import test_bp
    from routes.order import order_bp
    from routes.web_routes import web_bp

    api.register_blueprint(web_bp)  # Web pages
    api.register_blueprint(customer_bp)
    api.register_blueprint(order_bp)
    api.register_blueprint(test_bp)

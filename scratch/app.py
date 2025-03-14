import logging
from logging.handlers import RotatingFileHandler

from config import app_config
from extensions import api, db, ma, migrate
from flask import Flask, current_app, g, has_app_context, request
from utils.StructuredLogger import CustomFormatter, StructuredLogger


def create_app(config_class=app_config) -> Flask:
    app = Flask(app_config.API_TITLE)
    app.config.from_object(config_class)
    configure_logging(app)
    configure_extensions(app)
    register_blueprints(api)

    @app.before_request
    def log_request():
        logger().bind(
            flask_request_method=request.method,
            flask_request_path=request.path,
        )

    @app.after_request
    def log_response(response):
        if response:
            status_code = response.status_code
            logger().bind(
                flask_response_status_code=status_code,
            )
            if status_code < 300:
                logger().info("FLASK_RESPONSE")
            elif status_code >= 500:
                logger().error("FLASK_RESPONSE")
            else:
                logger().warning("FLASK_RESPONSE")

        return response

    return app


def logger():
    if not has_app_context():
        # unit tests for example might not have an app context
        return logging.Logger("scratch")
    if "logger" not in g:
        # cache a new instance in g which is scoped to the curent request
        g.logger = StructuredLogger(current_app.logger)
    return g.logger


def configure_logging(app: Flask) -> None:
    console_handler = logging.StreamHandler()
    # pretty json-formatted logs are great for readability, but too bulky for most environments
    console_handler.setFormatter(
        CustomFormatter(pretty_format_json=app_config.VERBOSE_LOGGING)
    )
    app.logger.addHandler(console_handler)

    # TODO: maxBytes and backupCount could come from config files?
    file_handler = RotatingFileHandler(
        "/tmp/scratch.log", maxBytes=1000000, backupCount=3
    )
    file_handler.setFormatter(CustomFormatter())
    app.logger.addHandler(file_handler)

    # TODO: what levels do we want per env?
    if app_config.ENVIRON in ("dev", "test"):
        app.logger.setLevel(logging.DEBUG)
    else:
        app.logger.setLevel(logging.INFO)


def configure_extensions(app: Flask) -> None:
    db.init_app(app)
    ma.init_app(app)
    api.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(api) -> None:

    from routes.customer import customer_bp
    from routes.error import error_bp
    from routes.health import health_bp
    from routes.order import order_bp
    from routes.web_routes import web_bp

    api.register_blueprint(health_bp)
    api.register_blueprint(customer_bp)
    api.register_blueprint(order_bp)
    api.register_blueprint(web_bp)  # Web pages
    api.register_blueprint(error_bp)

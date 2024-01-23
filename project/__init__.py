from flask import Flask
from logging.handlers import RotatingFileHandler
import logging
from flask.logging import default_handler
import os


# Application factory function
def create_app():
    app = Flask(__name__)

    config_type = os.getenv("CONFIG_TYPE", default="config.DevelopmentConfig")
    app.config.from_object(config_type)

    register_blueprints(app)
    configure_logging(app)

    return app


def register_blueprints(app):
    from project.stocks import stocks_blueprint
    from project.users import users_blueprint

    app.register_blueprint(stocks_blueprint)
    app.register_blueprint(users_blueprint, url_prefix="/users")


def configure_logging(app):
    file_handler = RotatingFileHandler(
        "instance/stock-portfolio.log", maxBytes=16384, backupCount=20
    )
    file_formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(message)s [in %(filename)s:%(lineno)d]"
    )
    file_handler.setFormatter(file_formatter)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.removeHandler(default_handler)

    app.logger.info("Starting the Stock Portfolio App...")

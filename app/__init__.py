import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import *

db = SQLAlchemy()


def create_app(config_class='Development'):
    
    app = Flask(__name__)
    app.config.from_object('app.{}'.format(config_class))

    db.init_app(app)
    
    from app.properties import properties_bp
    app.register_blueprint(properties_bp)

    from app.properties import models

    return app

if __name__ == "__main__":
    create_app()
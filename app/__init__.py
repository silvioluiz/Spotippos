import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Development


db = SQLAlchemy()
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "properties.db"))

#def create_app(config_class=Config):
def create_app():    
    app = Flask(__name__)
    app.config.from_object(Development)

    db.init_app(app)
    
    from app.properties import properties_bp
    app.register_blueprint(properties_bp)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = database_file
    
    return app

from app.properties import models
from flask import Flask


def create_app():
    app = Flask(__name__)
    from app.properties import properties_bp
    app.register_blueprint(properties_bp)
    
    return app

from flask import Blueprint

properties_bp = Blueprint('properties', __name__)

from app.properties import routes
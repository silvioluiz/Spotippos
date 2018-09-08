from app.properties import properties_bp
from flask import request

@properties_bp.route('/properties', methods=['POST'])
def createProperties():
    pass

@properties_bp.route('/properties/<id>')
def findProperty(id):
    pass

@properties_bp.route('/properties')
def searchProperties():
    pass


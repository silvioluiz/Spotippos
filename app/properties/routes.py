
import os
import json
from flask import request, abort, jsonify, make_response, Response
from jsonschema import validate, ErrorTree, Draft4Validator as Validator

from app.properties import properties_bp
from .models import Property
from .repositories import PropertyRepository as Repository

@properties_bp.route('/properties', methods=['POST'])
def createProperties():
    if (not request.is_json):
        abort(make_response(jsonify(message='Payload or mime type is not valid'), 415))
    else:
        errors = Validator(_load_schema('property.schema')).iter_errors(request.get_json())
        response_error = _errors(errors)
        if (response_error):
            resp = Response(response_error,
                status=422,
                mimetype="application/json")
            return resp
        else:
            prop = Property(**request.get_json())
            Repository.create(prop)
            return jsonify(prop.as_dict()), 201

@properties_bp.route('/properties/<id>')
def findProperty(id):
    pass

@properties_bp.route('/properties')
def searchProperties():
    pass

@properties_bp.errorhandler(400)
def bad_request(e):
    return jsonify(error=400, text=str(e)), 400
    
def _load_schema(filename):
    dir = os.path.dirname(__file__)
    file_path = os.path.join(dir, ('schemas/%s' % filename))
    with open(file_path, 'r') as schema_file:
        data = json.load(schema_file)
    return data

def _errors(errors):
    lista = []
    response_error = ''
    for error in errors:
        msg = '{"field":"%s","message":"%s"}' % (''.join(error.path), error.message)
        lista.append(msg)
    if (lista):
        response_error = '{"errors": [%s]}' % (','.join(lista))
    return response_error
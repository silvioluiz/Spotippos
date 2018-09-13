import os
import json
from flask import request, abort, jsonify, make_response, Response
from jsonschema import validate, ErrorTree, Draft4Validator as Validator

from app.properties import properties_bp
from .models import Property
from .repositories import PropertyRepository as Repository
from .utils import load

@properties_bp.route('/properties', methods=['POST'])
def create_properties():
    if (not request.is_json):
        abort(make_response(jsonify(message='Mime type is not valid'), 415))
    else:
        errors = Validator(load('schemas/property.schema')).iter_errors(request.get_json())
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
def find_property(id):
    prop = Repository.find_by_id(id);
    if (not prop):
        message = 'Property id {} not found'.format(id)
        abort(make_response(jsonify(message=message), 404))
    return jsonify(prop.as_dict()), 200

@properties_bp.route('/properties')
def search_properties():
    
    upper_x = request.args['ax']
    upper_y = request.args['ay']
    bottom_x = request.args['bx']
    bottom_y = request.args['by']
    
    params_json = '{"ax":%s, "ay":%s, "bx":%s, "by":%s  }' % (upper_x, upper_y, bottom_x, bottom_y)
    errors = Validator(load('schemas/filter.schema')).iter_errors(json.loads(params_json))
    
    response_error = _errors(errors)
    if (response_error):
        resp = Response(response_error,
            status=422,
            mimetype="application/json")
        return resp
    
    result = Repository.find_properties(upper_x, bottom_x, bottom_y, upper_y)
    if(not result):
        message = 'No properties found with these coordinates'
        abort(make_response(jsonify(message=message), 404))
    else:
        response = '{ "foundProperties": %s, "properties": %s }' % (len(result), json.dumps(result, ensure_ascii=False)) #, )
        return Response(response,
                status=200,
                mimetype="application/json")

@properties_bp.errorhandler(400)
def bad_request(e):
    return jsonify(error=400, text=str(e)), 400

def _errors(errors):
    lista = []
    response_error = ''
    for error in errors:
        msg = '{"field":"%s","message":"%s"}' % (''.join(error.path), error.message)
        lista.append(msg)
    if (lista):
        response_error = '{"errors": [%s]}' % (','.join(lista))
    return response_error
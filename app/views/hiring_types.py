from flask import jsonify
from flask.globals import request
from app.db.mongodb.hiring_types import new_hiring_type, find_all_hiring_types

def get_hiring_types():
    response_object = {'status': 'success'}
    response_object['hiring_types'] = find_all_hiring_types()
    if request.method == 'PATCH':
        patch_data = request.json
        new_hiring_type(patch_data)
    response = jsonify(response_object)
    return response

from flask import jsonify
from flask.globals import request
from app.db.mongodb.offices import new_office, find_all_offices

def get_offices():
    response_object = {'status': 'success'}
    response_object['offices'] = find_all_offices()
    if request.method == 'PATCH':
        patch_data = request.json
        new_office(patch_data)
    response = jsonify(response_object)
    return response

from flask import jsonify
from flask.globals import request
from app.db.mongodb.benefits import new_benefit, find_all_benefits

def get_benefits():
    response_object = {'status': 'success'}
    response_object['benefits'] = find_all_benefits()
    if request.method == 'PATCH':
        patch_data = request.json
        new_benefit(patch_data)
    response = jsonify(response_object)
    return response

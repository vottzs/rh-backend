from flask import jsonify
from app.db.mongodb.hiring_stages import find_one

def get_hiring_stages():
    response_object = {'status': 'success'}
    database_result = find_one()
    response_object['hiring_stages'] = database_result['values']
    response = jsonify(response_object)
    return response

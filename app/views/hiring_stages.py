
from flask import jsonify
from app.db.mongodb.hiring_stages import find_one

def get_hiring_stages():
    """
    Returns the list of default hiring stages.

    Return:
        response: JSON object with the default hiring stage information 
    """
    response_object = {'status': 'success'}
    database_result = find_one()
    response_object['hiring_stages'] = database_result['values']
    response = jsonify(response_object)
    return response

from flask import jsonify
from flask.globals import request
from app.db.mongodb.hiring_types import new_hiring_type, find_all_hiring_types

def get_hiring_types():
    """
    Returns all hiring types information or add a new hiring type to the database.

    Return:
        response: JSON object with hiring type information
    """
    response_object = {'status': 'success'}

    #recover all hiring types information
    response_object['hiring_types'] = find_all_hiring_types()
    #if the request method is PATCH, add a new hiring type to the database
    if request.method == 'PATCH':
        #recover data sent from frontend
        patch_data = request.json
        #add new hiring type on database
        new_hiring_type(patch_data)
    response = jsonify(response_object)
    return response

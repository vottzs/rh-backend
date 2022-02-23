from flask import jsonify
from flask.globals import request
from app.db.mongodb.offices import new_office, find_all_offices

def get_offices():
    """
    Returns all offices information or add a new office to the database.

    Return:
        response: JSON object with offices information
    """
    response_object = {'status': 'success'}
    #recover all offices information
    response_object['offices'] = find_all_offices()
    #if the request method is PATCH, add a new office to the database
    if request.method == 'PATCH':
        #recover data sent from frontend
        patch_data = request.json
        #add new office on database
        new_office(patch_data)
    response = jsonify(response_object)
    return response

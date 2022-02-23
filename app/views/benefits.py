from flask import jsonify
from flask.globals import request
from app.db.mongodb.benefits import new_benefit, find_all_benefits

def get_benefits():
    """
    Returns all benefits information or add a new benefit to the database.

    Return:
        response: JSON object with benefits information
    """
    response_object = {'status': 'success'}
    #recover all benefits information
    response_object['benefits'] = find_all_benefits()
    #if the request method is PATCH, add a new benefit to the database
    if request.method == 'PATCH':
        #recover data sent from frontend
        patch_data = request.json
        #add new office on database
        new_benefit(patch_data)
    response = jsonify(response_object)
    return response

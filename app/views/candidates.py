from flask import jsonify
from flask.globals import request
from app.db.mongodb.candidates import find_all, find_by_stage, find_one, move_candidate, new_candidate

def get_candidates():
    """
    Returns the list of cadidates, based on the criteria informed on the request.

    Return:
        response: JSON object with candidates information
    """
    stage = request.args.get('stage')
    response_object = {'status': 'success'}
    if stage is not None:
        response_object['candidates'] = find_by_stage(stage)
    else:
        response_object['candidates'] = find_all()
    response = jsonify(response_object)
    return response

def get_candidate(candidate_id):
    """
    Returns or updates a candidate for an given id.

    Params:
        candidate_id (string): candidate identifier

    Return:
        response: JSON object with candidate information
    """
    response_object = {'status': 'success'}
    #if candidate_id is not information, return error
    if candidate_id is None:
        return {'status': 'failed'}

    #candidate identifier is recorded as an integer number.
    # as it was informed as a text (string), it needs to be converted
    candidate_id = int(candidate_id)
    #recover most updated information about the candidate
    candidate = find_one((candidate_id))
    #if the request method is PATCH, update the candidate Stage
    if request.method == 'PATCH':
        #recover data sent from frontend
        patch_data = request.json
        #check if stage was informed
        if 'stage' in patch_data:
            #update candidate stage on database
            move_candidate((candidate_id), patch_data['stage'])
    #include candidate information on the response
    response_object['candidate'] = candidate
    #transform response to a JSON format
    response = jsonify(response_object)
    return response

def create_candidate():
    response_object = {'status': 'success'}
    patch_data = request.json
    new_candidate(patch_data)
    response = jsonify(response_object)
    return response
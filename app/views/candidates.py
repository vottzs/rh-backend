from flask import jsonify
from flask.globals import request
from app.db.mongodb.candidates import find_all, find_by_stage, find_one, move_candidate


def get_candidates():
    """
    Returns the list of candidates, based on the criteria informed on the request.

    Return:
        response: JSON object with the candidates information    
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
    Returns a candidate for an given id.

    Params:
        candidate_id (string): candidate identifier

    Return:
        response: JSON object with the candidate information 
    """
    response_object = {'status': 'success'}
    # if candidate_id is not information, return error
    if candidate_id is None:
        return {'status': 'failed'}

    # candidate identifier is recorded as an integer number.
    # as it was informed as a text (string), it needs to be converted
    candidate_id = int(candidate_id)
    # recover most updated information about the candidate
    candidate = find_one(candidate_id)
    # include candidate information on the response
    response_object['candidate'] = candidate
    # transform response to a JSON format
    response = jsonify(response_object)
    return response


def update_candidate(candidate_id):

    """
    Updates a candidate for an given id.

    Params:
        candidate_id (string): candidate identifier

    Return:
        response: JSON object with the candidate information 
    """
    response_object = {'status': 'success'}
    # if candidate_id is not information, return error
    if candidate_id is None:
        return {'status': 'failed'}

    # candidate identifier is recorded as an integer number.
    # as it was informed as a text (string), it needs to be converted
    candidate_id = int(candidate_id)
    # recover data sent from frontend
    patch_data = request.json
    # check if stage was informed
    if 'stage' in patch_data:
        # update candidate stage on database
        move_candidate(candidate_id, patch_data['stage'])
    return response_object
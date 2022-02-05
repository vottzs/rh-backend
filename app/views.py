"""
Module responsible for handle requests from a frontend.
"""
from unittest.mock import patch
from flask import Flask, jsonify
from flask.globals import request
from app.db.mocked_data import JOB_POSTINGS
from app.db.mongodb import hiring_stages, candidates

def add_views(app: Flask):
    """
    Maps urls and functions to the Flask application.

    Args:
        app (Flask): the rh-backend app
    """
    app.add_url_rule('/api/v1/hiring_stages', view_func=get_hiring_stages)
    app.add_url_rule('/api/v1/candidates', view_func=get_candidates)
    app.add_url_rule('/api/v1/candidates/<candidate_id>', view_func=get_candidate, methods=['GET', 'PATCH'])
    app.add_url_rule('/api/v1/job_postings', view_func=get_job_postings)


def get_hiring_stages():
    """
    Returns the list of default hiring stages.

    Return:
        response: JSON object with the default hiring stage information 
    """
    response_object = {'status': 'success'}
    database_result = hiring_stages.find_one()
    response_object['hiring_stages'] = database_result['values']
    response = jsonify(response_object)
    return response


def get_candidates():
    """
    Returns the list of candidates, based on the criteria informed on the request.

    Return:
        response: JSON object with the candidates information    
    """
    stage = request.args.get('stage')
    response_object = {'status': 'success'}
    if stage is not None:
        response_object['candidates'] = candidates.find_by_stage(stage)
    else:
        response_object['candidates'] = candidates.find_all()
    response = jsonify(response_object)
    return response

    
def get_job_postings():
    response_object = {'status': 'success'}
    response_object['job_postings'] = JOB_POSTINGS
    response = jsonify(response_object)
    return response


def get_candidate(candidate_id):
    """
    Operations related to a candidate for an given id.

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
    # if frontend is requesting an update
    if request.method == 'PATCH':
        # recover data sent from frontend
        patch_data = request.json
        # check if stage was informed
        if 'stage' in patch_data:
            # update candidate stage on database
            candidates.move_candidate(candidate_id, patch_data['stage'])
    # recover most updated information about the candidate
    candidate = candidates.find_one(candidate_id)
    # include candidate information on the response
    response_object['candidate'] = candidate
    # transform response to a JSON format
    response = jsonify(response_object)
    return response

from flask import Flask, jsonify
from flask.globals import request
from app.db.mocked_data import DEFAULT_HIRING_STAGES, CANDIDATES, JOB_POSTINGS

def add_views(app: Flask):
    app.add_url_rule('/api/v1/hiring_stages', view_func=get_hiring_stages)
    app.add_url_rule('/api/v1/candidates', view_func=get_candidates)
    app.add_url_rule('/api/v1/candidates/<candidate_id>', view_func=get_candidate, methods=['GET', 'PATCH'])
    app.add_url_rule('/api/v1/job_postings', view_func=get_job_postings)


def get_hiring_stages():
    response_object = {'status': 'success'}
    response_object['hiring_stages'] = DEFAULT_HIRING_STAGES
    response = jsonify(response_object)
    return response


def get_candidates():
    Stage = request.args.get('Stage')
    response_object = {'status': 'success'}
    if Stage is not None:
        filtered_cadidates = []
        for candidate in CANDIDATES:
            if candidate['Stage'] == Stage:
                filtered_cadidates.append(candidate)
        response_object['candidates'] = filtered_cadidates
    else:
        response_object['candidates'] = CANDIDATES
    response = jsonify(response_object)
    return response

    
def get_job_postings():
    response_object = {'status': 'success'}
    response_object['job_postings'] = JOB_POSTINGS
    response = jsonify(response_object)
    return response


def get_candidate(candidate_id):
    response_object = {'status': 'success'}
    candidate = search_on_list(CANDIDATES, 'id', int(candidate_id))
    if request.method == 'PATCH':
        patch_data = request.json
        candidate['Stage'] = patch_data ['Stage']
    response_object['candidate'] = candidate
    response = jsonify(response_object)
    return response


def search_on_list(list_of_dicts, key, value):
    return next(item for item in list_of_dicts if item.get(key) == value)

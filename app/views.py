
from flask import Flask, jsonify
from flask.globals import request
from app.db.mocked_data import JOB_POSTINGS
from app.db.mongodb import hiring_stages, candidates

def add_views(app: Flask):
    app.add_url_rule('/api/v1/hiring_stages', view_func=get_hiring_stages)
    app.add_url_rule('/api/v1/candidates', view_func=get_candidates)
    app.add_url_rule('/api/v1/candidates/<candidate_id>', view_func=get_candidate, methods=['GET', "PATCH"])
    app.add_url_rule('/api/v1/job_postings', view_func=get_job_postings)


def get_hiring_stages():
    response_object = {'status': 'success'}
    database_result = hiring_stages.find_one()
    response_object['hiring_stages'] = database_result['values']
    response = jsonify(response_object)
    return response


def get_candidates():
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
    response_object = {'status': 'success'}
    if candidate_id is None:
        return {'status': 'failed'}
    candidate_id = int(candidate_id)
    candidate = candidates.find_one(candidate_id)
    if request.method == 'PATCH':
        patch_data = request.json
        if 'stage' in patch_data:
            candidates.move_candidate(candidate_id, patch_data['stage'])
    response_object['candidate'] = candidate
    response = jsonify(response_object)
    return response

    

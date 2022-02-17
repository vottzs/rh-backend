from flask import Flask, jsonify
from flask.globals import request
from app.db.mocked_data import JOB_POSTINGS
from app.db.mongodb import hiring_stages, candidates, offices, benefits, hiring_types

def add_views(app: Flask):
    app.add_url_rule('/api/v1/hiring_stages', view_func=get_hiring_stages)
    app.add_url_rule('/api/v1/candidates', view_func=get_candidates)
    app.add_url_rule('/api/v1/candidates/<candidate_id>', view_func=get_candidate, methods=['GET', 'PATCH'])
    app.add_url_rule('/api/v1/job_postings', view_func=get_job_postings)
    app.add_url_rule('/api/v1/offices', view_func=get_offices, methods=['GET', 'PATCH'])
    app.add_url_rule('/api/v1/benefits', view_func=get_benefits, methods=['GET', 'PATCH'])
    app.add_url_rule('/api/v1/hiring_types', view_func=get_hiring_types, methods=['GET', 'PATCH'])


def get_hiring_stages():
    response_object = {'status': 'success'}
    database_result = hiring_stages.find_one()
    response_object['hiring_stages'] = database_result['values']
    response = jsonify(response_object)
    return response


def get_candidates():
    Stage = request.args.get('Stage')
    response_object = {'status': 'success'}
    if Stage is not None:
        response_object['candidates'] = candidates.find_by_stage(Stage)
    else:
        response_object['candidates'] = candidates.find_all()
    response = jsonify(response_object)
    return response

def get_job_postings():
    response_object = {'status': 'success'}
    response_object['job_postings'] = JOB_POSTINGS
    response = jsonify(response_object)
    return response

def get_offices():
    response_object = {'status': 'success'}
    response_object['offices'] = offices.find_all_offices()
    if request.method == 'PATCH':
        patch_data = request.json
        offices.new_office(patch_data)
    response = jsonify(response_object)
    return response

def get_benefits():
    response_object = {'status': 'success'}
    response_object['benefits'] = benefits.find_all_benefits()
    if request.method == 'PATCH':
        patch_data = request.json
        benefits.new_benefit(patch_data)
    response = jsonify(response_object)
    return response

def get_hiring_types():
    response_object = {'status': 'success'}
    response_object['hiring_types'] = hiring_types.find_all_hiring_types()
    if request.method == 'PATCH':
        patch_data = request.json
        hiring_types.new_hiring_type(patch_data)
    response = jsonify(response_object)
    return response

def get_candidate(candidate_id):
    response_object = {'status': 'success'}
    if candidate_id is None:
        return {'status': 'failed'}
    candidate_id = int(candidate_id)
    candidate = candidates.find_one((candidate_id))
    if request.method == 'PATCH':
        patch_data = request.json
        candidates.move_candidate((candidate_id), patch_data['Stage'])
    response_object['candidate'] = candidate
    response = jsonify(response_object)
    return response


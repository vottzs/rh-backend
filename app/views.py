from flask import Flask, jsonify
from app.db.mocked_data import DEFAULT_HIRING_STAGES
from app.db.mocked_data import JOB_BENEFITS_OPTIONS
from app.db.mocked_data import HIRING_TYPES
from app.db.mocked_data import CANDIDATES
from app.db.mocked_data import OFFICES
from app.db.mocked_data import JOB_POSTINGS

def add_views(app: Flask):
    app.add_url_rule('api/v1/hiring_stages', view_func=get_hiring_stages)
    app.add_url_rule('api/v1/job_benefits_options', view_func=get_job_benefits_options)
    app.add_url_rule('api/v1/candidates' , view_func=get_candidates)

def get_hiring_stages():
    response_object = {'status': 'success'}
    response_object['hiring_stages'] = DEFAULT_HIRING_STAGES
    response = jsonify(response_object)
    return response

def get_job_benefits_options():
    response_object = {'status': 'success'}
    response_object['job_benefits_options'] = JOB_BENEFITS_OPTIONS
    response = jsonify(response_object)
    return response

def get_candidates():
    response_object = {'status': 'success'}
    response_object['candidates'] = CANDIDATES
    response = jsonify(response_object)
    return response   
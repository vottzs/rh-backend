from flask import Flask, jsonify
from app.db.mocked_data import DEFAULT_HIRING_STAGES
from app.db.mocked_data import JOB_BENEFITS_OPTIONS
from app.db.mocked_data import HIRING_TYPES
from app.db.mocked_data import HIRING_STAGES
from app.db.mocked_data import CANDIDATES
from app.db.mocked_data import OFFICES
from app.db.mocked_data import JOB_POSTINGS

def add_views(app: Flask):
    app.add_url_rule('/api/v1/hiring_stages', view_func=get_hiring_stages)
    app.add_url_rule('/api/v1/job_benefits_options', view_func=job_benefits_options)
    app.add_url_rule('/api/v1/hiring_types', view_func=hiring_types)
    app.add_url_rule('/api/v1/hiring_stages', view_func=hiring_stages)
    app.add_url_rule('/api/v1/candidates', view_func=candidates)
    app.add_url_rule('/api/v1/offices', view_func=offices)
    app.add_url_rule('/api/v1/job_postings', view_func=job_postings)

def get_hiring_stages():
    response_object = {'status': 'success'}
    response_object['hiring_stages'] = DEFAULT_HIRING_STAGES
    response = jsonify(response_object)
    return response

def job_benefits_options():
    response_object = {'status': 'success'}
    response_object['job_benefits_options'] = JOB_BENEFITS_OPTIONS
    response = jsonify(response_object)
    return response
    
def hiring_types():
    response_object = {'status':'success'}
    response_object['hiring_types'] = HIRING_TYPES
    response = jsonify(response_object)
    return response

def hiring_stages():
    response_object = {'status':'success'}
    response_object['hiring_Stages'] = HIRING_STAGES
    response = jsonify(response_object)
    return response

def candidates():
    response_object = {'status':'success'}
    response_object['candidates'] = CANDIDATES
    response = jsonify(response_object)
    return response

def offices():
    response_object = {'status':'success'}
    response_object['offices'] = OFFICES
    response = jsonify(response_object)
    return response

def job_postings():
    response_object = {'status':'success'}
    response_object['job_postings'] = JOB_POSTINGS
    response = jsonify(response_object)
    return response
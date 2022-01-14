from flask import Flask, jsonify
from app.db.mocked_data import CARROS, DEFAULT_HIRING_STAGES
from app.db.mocked_data import CANDIDATES
from app.db.mocked_data import JOB_POSTINGS

def add_views(app: Flask):
    app.add_url_rule('/api/v1/hiring_stages', view_func=get_hiring_stages)
    app.add_url_rule('/api/v1/candidates', view_func=get_candidates)
    app.add_url_rule('/api/v1/job_postings', view_func=get_job_postings)
    app.add_url_rule('/api/v1/carros', view_func=get_cars)
    #app.add_url_rule('/api/v1/carros/<car>', view_func=get_car)

def get_hiring_stages():
    response_object = {'status': 'success'}
    response_object['hiring_stages'] = DEFAULT_HIRING_STAGES
    response = jsonify(response_object)
    return response

def get_candidates():
    response_object = {'status': 'sucess'}
    response_object['candidates'] = CANDIDATES
    response = jsonify(response_object)
    return response
    
def get_job_postings():
    response_object = {'status': 'sucess'}
    response_object['job_postings'] = JOB_POSTINGS
    response = jsonify(response_object)
    return response

def get_cars():
    response_object = {'status': 'sucess'}
    response_object['carros'] = CARROS
    response = jsonify(response_object)
    return response
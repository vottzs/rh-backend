from flask import Flask, jsonify
from app.models import HIRING_STAGES

def add_views(app: Flask):
    app.add_url_rule('/hiring_stages', view_func=get_hiring_stages)

def get_hiring_stages():
    response_object = {'status': 'success'}
    response_object['hiring_stages'] = HIRING_STAGES
    response = jsonify(response_object)
    return response

    def add_views(app: Flask):
    app.add_url_rule('/candidates', view_func=get_candidates)

    def get_candidates():
    response_object = {'status': 'success'}
    response_object['candidates'] = CANDIDATES
    response = jsonify(response_object)
    return response

    def add_views(app: Flask):
    app.add_url_rule('/job_posting', view_func=get_job_posting)

    def get_candidates():
    response_object = {'status': 'success'}
    response_object['job_posting'] = JOB_POSTING
    response = jsonify(response_object)
    return response


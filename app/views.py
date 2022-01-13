from flask import Flask, jsonify
from app.db.mocked_data import DEFAULT_HIRING_STAGES

def add_views(app: Flask):
    app.add_url_rule('/hiring_stages', view_func=get_hiring_stages)

def get_hiring_stages():
    response_object = {'status': 'success'}
    response_object['hiring_stages'] = DEFAULT_HIRING_STAGES
    response = jsonify(response_object)
    return response

#create the Candidates endpoints
from flask import Flask, jsonify
from app.db.mocked_data import CANDIDATES

def add_views(app: Flask):
    app.add_url_rule('/candidates', view_func=get_candidates)

def get_candidates():
    response_object = {'status': 'success'}
    response_object['candidates'] = CANDIDATES
    response = jsonify(response_object)
    return response

    #create the job posting endpoints
from flask import Flask, jsonify
from app.db.mocked_data import JOB_POSTINGS

def add_views(app: Flask):
    app.add_url_rule('/job_postings', view_func=get_job_postings)

def get_job_postings():
    response_object = {'status': 'success'}
    response_object['job_postings'] = JOB_POSTINGS
    response = jsonify(response_object)
    return response
from flask import Flask, jsonify
from app.db.mocked_data import HIRING_STAGES

def add_views(app: Flask):
    app.add_url_rule('/hiring_stages', view_func=get_hiring_stages)

def get_hiring_stages():
    response_object = {'status': 'success'}
    response_object['hiring_stages'] = HIRING_STAGES
    response = jsonify(response_object)
    return response

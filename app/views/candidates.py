from flask import jsonify
from flask.globals import request
from app.db.mongodb.candidates import find_all, find_by_stage, find_one, move_candidate

def get_candidates():
    stage = request.args.get('stage')
    response_object = {'status': 'success'}
    if stage is not None:
        response_object['candidates'] = find_by_stage(stage)
    else:
        response_object['candidates'] = find_all()
    response = jsonify(response_object)
    return response

def get_candidate(candidate_id):
    response_object = {'status': 'success'}
    if candidate_id is None:
        return {'status': 'failed'}
    candidate_id = int(candidate_id)
    candidate = find_one((candidate_id))
    if request.method == 'PATCH':
        patch_data = request.json
        move_candidate((candidate_id), patch_data['stage'])
    response_object['candidate'] = candidate
    response = jsonify(response_object)
    return response
from flask import jsonify
from flask.globals import request
from app.db.mongodb.job_postings import new_job_posting, find_all_job_postings, find_one

def get_job_postings():
    """
    Returns all job postings information or add a new job posting to the database or resets all job postings stages to inactive

    Return:
        response: JSON object with the job postings information
    """
    stage = request.args.get('stage')
    response_object = {'status': 'success'}
        #recover job_postings information for a given stage
    if stage is not None:
        response_object['job_postings'] = find_by_stage(stage)
    else:
        #recover all job_postings information
        response_object['job_postings'] = find_all_job_postings()
    #if the request method is POST, set all job_postings stage to inactive
    #if the request method is PATCH, add a new job_posting to the database
    if request.method == 'PATCH':
        #recover data sent from frontend
        patch_data = request.json
        #add new office on database
        new_job_posting(patch_data)
    response = jsonify(response_object)
    return response

def get_job_posting(_id):
    response_object = {'status': 'success'}
    #if job_posting_title is not information, return error
    if _id is None:
        return {'status': 'failed'}
    #recover most updated information about the job_posting
    job_posting = find_one((_id))
    #if the request method is PATCH, update the job_posting Stage
    #include job_posting information on the response
    response_object['job_posting'] = job_posting
    #transform response to a JSON format
    response = jsonify(response_object)
    return response

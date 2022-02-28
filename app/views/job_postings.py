from flask import jsonify
from flask.globals import request
from app.db.mongodb.job_postings import new_job_posting, find_all_job_postings, find_one, activate_job_posting, find_by_stage, reset_job_postings, find_one_to_export

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
    if request.method == 'POST':
        #recover data sent from frontend
        patch_data = request.get_json()
        #check if stage was informed
        if 'stage' in patch_data:
            #update job_posting stage on database
            reset_job_postings(patch_data['stage'])
    #if the request method is PATCH, add a new job_posting to the database
    if request.method == 'PATCH':
        #recover data sent from frontend
        patch_data = request.json
        #add new office on database
        new_job_posting(patch_data)
    response = jsonify(response_object)
    return response

def get_job_posting(job_posting_tittle):
    response_object = {'status': 'success'}
    #if job_posting_tittle is not information, return error
    if job_posting_tittle is None:
        return {'status': 'failed'}
    #recover most updated information about the job_posting
    job_posting = find_one((job_posting_tittle))
    #if the request method is PATCH, update the job_posting Stage
    if request.method == 'PATCH':
        #recover data sent from frontend
        patch_data = request.get_json()
        #check if stage was informed
        if 'stage' in patch_data:
            #update job_posting stage on database
            activate_job_posting((job_posting_tittle), patch_data['stage'])
    #include job_posting information on the response
    response_object['job_posting'] = job_posting
    #transform response to a JSON format
    response = jsonify(response_object)
    return response

def export_job_posting(stage):
    """
    Returns a job_posting for an given stage.

    Params:
        stage (string): job_posting identifier

    Return:
        response: JSON object with job_posting information
    """
    response_object = {'status': 'success'}
    #if job_posting is not information, return error
    if stage is None:
        return {'status': 'failed'}

    #recover most updated information about the job_posting
    job_posting = find_one_to_export((stage))
    response_object['job_posting'] = job_posting
    #transform response to a JSON format
    response = jsonify(response_object)
    return response
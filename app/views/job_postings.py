from flask import jsonify
from flask.globals import request
from app.db.mongodb.job_postings import new_job_posting, find_all_job_postings

def get_job_postings():
    """
    Returns all job postings information or add a new job posting to the database.

    Return:
        response: JSON object with the job postings information
    """
    response_object = {'status': 'success'}
    #recover all offices information
    response_object['job_postings'] = find_all_job_postings()
    #if the request method is PATCH, add a new office to the database
    if request.method == 'PATCH':
        #recover data sent from frontend
        patch_data = request.json
        #add new office on database
        new_job_posting(patch_data)
    response = jsonify(response_object)
    return response

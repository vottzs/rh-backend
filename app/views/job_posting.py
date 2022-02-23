from flask import jsonify
from app.db.mocked_data import JOB_POSTINGS

def get_job_postings():
    """
    Returns the list of job postings.

    Return:
        response: JSON object with the job postings information
    """
    response_object = {'status': 'success'}
    response_object['job_postings'] = JOB_POSTINGS
    response = jsonify(response_object)
    return response

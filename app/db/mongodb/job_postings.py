"""
All database operations related to job_postings.
"""
from app.db.mongodb import DATABASE
from bson import ObjectId

def parse_job_postings(job_postings):
    for item in job_postings:
        item['_id'] = str(item['_id'])

def new_job_posting(new_job_posting_var):
    """
    Creates  a new job posting.
    Args:
        new_job_posting_var (dict): new job posting information
    """
    DATABASE.job_postings.insert_one(new_job_posting_var)

def find_all_job_postings ():
    """
    Returns all job_postings from database
    """
    result = list(DATABASE.job_postings.find({}))
    parse_job_postings(result)
    return result

def find_one(_id):
    """
    Returns one job_posting 
    
    Args:
        job_posting_title (int): job_posting identifier
    Returns:
        result (dict): job_posting information
    """
    #_id (ObjectId) is not needed, {'_id': False} filters that from database
    result = DATABASE.job_postings.find_one({'_id': ObjectId(_id)})
    result['_id'] = str(result['_id'])
    return result

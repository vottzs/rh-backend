"""
All database operations related to job_postings.
"""
from app.db.mongodb import DATABASE

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
    result = list(DATABASE.job_postings.find({}, {'_id': False}))
    return result

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

def find_one(job_posting_title):
    """
    Returns one job_posting 
    
    Args:
        job_posting_title (int): job_posting identifier
    Returns:
        result (dict): job_posting information
    """
    #_id (ObjectId) is not needed, {'_id': False} filters that from database
    result = DATABASE.job_postings.find_one({'title': job_posting_title}, {'_id': False})
    return result

def find_one_to_export(stage):
    """
    Returns one job_posting 
    
    Args:
        stage (string): job_posting identifier
    Returns:
        result (dict): job_posting information
    """
    #_id (ObjectId) is not needed, {'_id': False} filters that from database
    result = DATABASE.job_postings.find_one({'stage': stage}, {'_id': False})
    return result

def activate_job_posting(job_posting_title, stage):
    """
    Updates the stage for a job_posting, moving it on the hiring workflow.
    Args:
        job_posting_title (int): job_posting identifier
        stage (string): new stage for the job_posting
    """
    #_id (ObjectId) is not needed, {'_id': False} filters that from database
    DATABASE.job_postings.update_one({'title': job_posting_title}, {'$set': {'stage': stage}})

def find_by_stage(stage):
    """
    Returns all job_postings in a given stage from database.
    Args:
        stage (string): which stage is expected
    
    Returns:
        result (list): job_postings with stage equals to the given stage
    """
    #_id (ObjectId) is not needed, {'_id': False} filters that from database
    result = list(DATABASE.job_postings.find({'stage': stage}, {'_id': False}))
    return result

def reset_job_postings(stage):
    """
    Updates the stage for a job_posting, moving it on the hiring workflow.
    Args:
        job_posting_id (int): job_posting identifier
        stage (string): new stage for the job_posting
    """
    #_id (ObjectId) is not needed, {'_id': False} filters that from database
    DATABASE.job_postings.update_one({'stage': stage}, {'$set': {'stage': 'inactive'}})

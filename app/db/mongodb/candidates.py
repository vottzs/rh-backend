"""
All database operations related to candidates.
"""
from app.db.mongodb import DATABASE

def find_all():
    """
    Returns all candidates from database
    """
    #_id (ObjectId) is not needed, {'_id': False} filters that from database
    result = list(DATABASE.candidates.find({}, {'_id': False}))
    return result

def find_by_stage(stage):
    """
    Returns all candidates in a given stage from database.

    Args:
        stage (string): which stage is expected
    
    Returns:
        result (list): candidates with stage equals to the given stage
    """
    #_id (ObjectId) is not needed, {'_id': False} filters that from database
    result = list(DATABASE.candidates.find({'stage': stage}, {'_id': False}))
    return result

def find_one(candidate_id):
    """
    Returns one candidate 
    
    Args:
        candidate_id (int): candidate identifier

    Returns:
        result (dict): candidate information
    """
    #_id (ObjectId) is not needed, {'_id': False} filters that from database
    result = DATABASE.candidates.find_one({'id': candidate_id}, {'_id': False})
    return result

def move_candidate(candidate_id, stage):
    """
    Updates the stage for a candidate, moving it on the hiring workflow.

    Args:
        candidate_id (int): candidate identifier
        stage (string): new stage for the candidate
    """
    #_id (ObjectId) is not needed, {'_id': False} filters that from database
    DATABASE.candidates.update_one({'id': candidate_id}, {'$set': {'stage': stage}})

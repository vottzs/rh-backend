"""
All database operations related to hiring_stages.
"""
from app.db.mongodb import DATABASE

def find_one():
    """
    Returns the default hiring stages 
    
    Returns:
        result (dict): default hiring stages information
    """
    #_id (ObjectId) is not needed, {'_id': False} filters that from database
    result = DATABASE.default_hiring_stages.find_one({}, {'_id': False})
    return result
    
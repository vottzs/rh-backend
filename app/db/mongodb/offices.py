"""
All database operations related to offices.
"""
from app.db.mongodb import DATABASE

def parse_offices(offices):
    for item in offices:
        item['_id'] = str(item['_id'])

def new_office(new_office_var):
    """
    Creates  a new office.
    Args:
        new_office_var (dict): new office information
    """
    DATABASE.offices.insert_one(new_office_var)

def find_all_offices ():
    """
    Returns all offices from database
    """
    result = list(DATABASE.offices.find({}))
    for item in result:
        #for every ObjectId transforms the _Id in a creation date
        item['creation_date'] = item['_id'].generation_time
    parse_offices(result)
    return result
